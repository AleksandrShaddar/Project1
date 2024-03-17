#  Напишите программу на Python, которая будет находить
# сумму элементов массива из 1000000 целых чисел.
# - Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# - Массив должен быть заполнен случайными целыми числами
# от 1 до 100.
# - При решении задачи нужно использовать многопоточность,
# многопроцессорность и асинхронность.
# - В каждом решении нужно вывести время выполнения
# вычислений.


import asyncio
import time
from random import randint


ARR = []
MIN = 1
MAX = 100
PARTS = 1000  # Задаем количество делений списка элементов ARR
RESULT = 0

for _ in range(1_000_000):
    ARR.append(randint(MIN, MAX))


def split_arr(array, parts=1):
    length = len(array)
    return [array[i*length // parts: (i+1)*length // parts]
            for i in range(parts)]


async def worker(arr):
    global RESULT
    RESULT += sum(arr)


async def main():
    for array in split_arr(ARR, parts=PARTS):
        task = asyncio.create_task(worker(array))
        await task


if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    print(sum(ARR))  # Для сверки првильности подсчета
    print(RESULT)  # Вывод результата
    print(f'Асинхронное программирование: {(time.time() - start):.3f} сек '
          f'при делении на {PARTS} частей')
