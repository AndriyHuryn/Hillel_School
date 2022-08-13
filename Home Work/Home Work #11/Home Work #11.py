"""
Створити text.txt файл в катаолозі з файлом ДЗ.
Створити програму, яка запитує у користувача назву файла.
1.Якщо такий файл існує - читає вміст, та виводить його в термінал. Якщо ж ні - виводить інформацію, що файла не існує
2.Якщо файл відкрився - програма запитує у користувача, що зробити з файлом. Можливі наступні опції:
     Прочитати останні 10 строк (read_last_10_lines)
     Прочитати перші 10 строк (read_first_10_lines)
     Прочитати весь файл (read_all_file)
     Знайти найбільше (найдовше) слово у файлі (find_longest_word)
     Вивести кількість строк (lines_number)
     Вийти з програми (exit)
3.Якщо користувач опцію, яка не передбачена вище - запитуємо в нього ще раз
Зірочка (не обовʼязково): Додати опцію words_frequency, яка виводить число повторень кожного слова в коді
"""
import re
from pathlib import Path
all_options = ("Please select following options:\n"+
               "To Read full file type - 1\n"
               "To Read first 10  lines type - 2\n"+
               "To Read last 10 lines type - 3\n"+
               "To Find longest word type - 4\n"+
               "To Find how many lines are type - 5\n"+
               "Enter Here:")
regex = r'\s|!\s|,\s|\.\s|\?\s'

def work_with_file(file):
    decision = input(f"{all_options}\n")
    file_lines = []
    for line in file:
        file_lines.append(line)

    if decision == "1":
        file = open(file_name, mode="r", encoding="utf-8")
        data = file.read()
        print(data)
        file.close()
    elif decision == "2":
        for i in range(10):
            print(file_lines[i])
    elif decision == "3":
        for i in range(len(file_lines)-10, len(file_lines)):
            print(file_lines[i])
    elif decision == "4":
        list_word = re.split(regex, "".join(file_lines))
        find_longest_word = list_word[0]
        for i in range(1, len(list_word)):
            if len(list_word[i]) > len(find_longest_word):
                find_longest_word = list_word[i]
        print(f"The longest word in the file is: '{find_longest_word}' and size of " + str(len(find_longest_word))+" characters")
    elif decision == "5":
        file = open(file_name, mode="r", encoding="utf-8")
        for count, line in enumerate(file):
            pass
        print("Total Lines ", count + 1)


file_name = input("Enter file name to see if we have it: ")
if Path(file_name).is_file():
    with open(file_name, mode='r', encoding="utf-8") as file:
        work_with_file(file)
else:
    print("Sorry we cannot find your file in our DB")
