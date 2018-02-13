import os
import os.path
import shutil

print(os.listdir())  # без аргументов перечислит файлы в текущей директории, можно указать имя папки ""
print(os.getcwd())  # чтобы узнать текущую папку

print(os.path.exists("def2.py"))
print(os.path.exists("def20.py"))

print(os.path.isfile("def2.py"))  # проверка, что папка

print(os.path.isdir("def2.py"))  # проверка, что директория

print(os.path.abspath("def2.py"))  # абсолютный путь по относительному

os.chdir("homework_part1")  # перейти в другую директорию
print(os.getcwd())

for current_dir, dirs, files in os.walk("."):  # рекурсивный проход по всем папкам, подпапкам и тд. ("." - текущая директория)
    print(current_dir, dirs, files)

shutil.copy("tests/test1.txt", "tests/test2.txt")  # копирование файла

for current_dir, dirs, files in os.walk("."):
    print(current_dir, dirs, files)

shutil.copytree("tests", "tests/tests")  # копирование папки

for current_dir, dirs, files in os.walk("."):
    print(current_dir, dirs, files)

