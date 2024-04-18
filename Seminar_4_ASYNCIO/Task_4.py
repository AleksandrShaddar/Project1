# Создать программу, которая будет производить подсчет 
# количества слов в каждом файле в указанной директории и 
# выводить результаты в консоль.
# Используйте потоки.

import threading
import os
import time


MY_PATH = '.'


def worker(file_):
    with open (file_, 'r', encoding='utf-8') as f:
        content = f.read()
        print(f'Слов в {file_} : {len(content.split())}')
    

start = time.time()
threads = []

for root, dirs, file_name in os.walk(MY_PATH):
    for f in file_name:
        t = threading.Thread(target=worker, args=(f,))
        threads.append(t)
        t.start()

for t in threads:
    t.join()

print (f'{(time.time() - start):.3f}')