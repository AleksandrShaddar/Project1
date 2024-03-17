#  Напишите программу на Python, которая будет находить
# сумму элементов массива из 1000000 целых чисел.
# - Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# - Массив должен быть заполнен случайными целыми числами
# от 1 до 100.
# - При решении задачи нужно использовать многопоточность,
# многопроцессорность и асинхронность.
# - В каждом решении нужно вывести время выполнения
# вычислений.


import multiprocessing
import time
from random import randint


ARR = []
MIN = 1
MAX = 100
PARTS = 10  # Задаем количество делений списка элементов ARR
RESULT = multiprocessing.Value('i', 0)

for _ in range(1_000_000):
    ARR.append(randint(MIN, MAX))


def split_arr(array, parts=1):
    length = len(array)
    return [array[i*length // parts: (i+1)*length // parts]
            for i in range(parts)]


def worker(arr, cnt):
    with cnt.get_lock():
        cnt.value += sum(arr)


if __name__ == '__main__':
    start = time.time()
    multiprocess = []

    for array in split_arr(ARR, parts=PARTS):
        t = multiprocessing.Process(target=worker, args=(array, RESULT))
        multiprocess.append(t)
        t.start()

    for t in multiprocess:
        t.join()

    # print(sum(ARR))  # Для сверки првильности подсчета
    print(RESULT.value)  # Вывод результата
    print(f'Многопроцессорность: {(time.time() - start):.3f} сек при делении '
          f'на {PARTS} частей')
