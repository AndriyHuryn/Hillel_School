"""
- Коли додаток запускаэться, три потоки (T1, T2, T3) стартують
- потік T1 заповнює список випадковими числами (10_000 елементів)
- потоки T2 та T3 очікую доки попередній список заповниться
- коли список заповнений T2 та T3 стартують
- потік T2 знаходить суму елементів у списку
- потік T3 знаходить середнє арифметичне для елементів у списку
- на екран виводяться результуючі 2 списки (2 список - вихідні дані з T2 та T3)"""

from threading import Thread
from random import  randint

list = []

n = int(input("Please input number of how many elements you like to be generated: "))

def thread1():
    for i in range(n):
        i = randint(1, n)
        list.append(i)
    print(f"Your list with given random of {n} number is:\n {list}")
    return list

def thread2():
    sum_elements = sum(list)
    print(f"The sum of all elements with random number of {n} in current list equal:\n {sum_elements}")
    return sum_elements

def thread3():
    avarage = sum(list)/len(list)
    print(f"The arithmetic average of your list with requested length of {n} is\n {avarage}")
    return avarage

t1 = Thread(target=thread1())
t2 = Thread(target=thread2())
t3 = Thread(target=thread3())

t1.start()
t1.join()
t2.start()
t3.start()
print("Let us know how did we do!!!")



