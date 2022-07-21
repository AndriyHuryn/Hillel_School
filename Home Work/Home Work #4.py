"""1) Дано: строка у якому є числа (розділяються пробілами)"""
"""Наприклад"""
"""43 більше ніж 34 але менше ніж 56"""
"""Знайти суму ВСІХ ЧИСЕЛ (А НЕ ЦИФР) у цьому рядку.
Для цього прикладу відповідь - 133. (використовуйте split і перевірку isdigit)"""

n = input()
sum = 0
list = n.split()
print(list)
for digit in list:
    if digit.isdigit():
        sum += int(digit)
print(sum)

"""2) Наведено список строк my_list.
Створити новий список, в який помістити елементи з my_list"""
"""у яких перший символ - буква "a". (велика буква "А" теж рахується)"""

list = 'Andriy is an adult and like to adventures. Dusty is as close as it is to Andriy as possible'
new_list = []
match = [a for a in list.split() if 'a' in a.casefold()]
new_list += match
print("Your new list is:", *new_list)


"""3) Напишіть програму, яка знаходить різницю між двома списками та зберігає її у новий список."""
l1 = ['One', 'Two', 'Three', 'Four', 12, 2]
l2 = ['One', 'Two']
list = list(set(l1)-set(l2))
print("Your 1st list is:", l1)
print("Your 2nd list is:", l2)
print("Your Differnece is recoreded into new list:", *list)

"""Second Option"""
list = []
for item in l1:
    if item not in l2:
        list.append(item)
print("Your 1st list is:", l1)
print("Your 2nd list is:", l2)
print("Your Difference is recorded into new list:", *list)


"""4) Дано: строка my_str. Поділіть цю строку на пари з двох символів"""
"""та помістіть ці пари до списку. Якщо рядок містить непарну кількість символів,"""
"""пропущений другий символ останньої пари має бути замінений на підкреслення ("_")."""
"""Приклади:"""
"""'abcd' -> ['ab', 'cd'],"""
"""'abcde' -> ['ab', 'cd', e_'] """
"""(використовуйте зрізи довжини 2)"""


my_str = "abcde"
my_list = []
elem = ''
for i in range (len(my_str)):
    elem+=my_str[i]
    if i%2 != 0:
        my_list.append(elem)
        elem=''
str_len= len(my_str)
if str_len%2!=0:
    my_list.append(my_str[str_len-1]+"_")

print(my_list)