# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


import os
import shutil
import sys

def list_dir(main_path):
    for _ in os.listdir(main_path):
        print(_)
main_path = os.getcwd()
list_dir(main_path)