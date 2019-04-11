import os
import sys


def change_direcrory():
    directory = input("Введите путь:")
    try:
        os.chdir(directory)
        print("Успешно перешёл\n")
    except Exception as e:
        print("Невозможно перейти! " + str(e))


def show_directory():
    content = os.listdir()
    for c in content:
        print(c)
    print("\n")


def remove_directory():
    directory = input("Введите название папки:")
    try:
        os.rmdir(directory)
        print("Успешно удалено\n")
    except Exception as e:
        print("Невозможно удалить! " + str(e))


def create_directory():
    directory = input("Введите название папки:")
    try:
        os.mkdir(directory)
        print("Успешно создано\n")
    except Exception as e:
        print("Невозможно создать! " + str(e))
