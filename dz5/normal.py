
# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import os
import sys
import EasyFolderActions as f1

help = """Выберите действие:
 1. Перейти в папку
 2. Просмотреть содержимое текущей папки
 3. Удалить папку
 4. Создать папку
 5. Выход
 \n"""

folder_actions = {
    "1": f1.change_direcrory,
    "2": f1.show_directory,
    "3": f1.remove_directory,
    "4": f1.create_directory
}

while True:
    action = input(help)

    if action == "5":
            break
    elif action:
        if folder_actions.get(action):
            folder_actions.get(action)()
