
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import sys
import shutil


def create_dirs():
    name_dir = "dir"
    base_dir_name = os.getcwd()
    for i in range(1, 10):
        os.mkdir(os.path.join(base_dir_name, f"{name_dir}_{i}"))


def delete_dirs():
    name_dir = "dir"
    base_dir_name = os.getcwd()
    for i in range(1, 10):
        os.rmdir(os.path.join(base_dir_name, f"{name_dir}_{i}"))

create_dirs()
delete_dirs()

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

files_in_current_dir = filter(os.path.isdir, os.listdir())
for f in files_in_current_dir:
    print(f)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


def copy_execute_file():
    full_name = sys.argv[0]
    shutil.copy(full_name, f"{full_name[:-3]}_copy.py")

copy_execute_file()
