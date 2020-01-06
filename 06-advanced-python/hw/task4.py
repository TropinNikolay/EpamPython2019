"""
Реализовать метод __str__, позволяющий выводить все папки и файлы из данной, например так:
> print(folder1)
V folder1
|-> V folder2
|   |-> V folder3
|   |   |-> file3
|   |-> file2
|-> file1
А так же возможность проверить, находится ли файл или папка в другой папке:
> print(file3 in folder2)
True
"""
import os


class PrintableFolder:
    def __init__(self, path):
        self.path = path

    def __str__(self):
        result = ""
        for root, dirs, files in os.walk(self.path):
            level = root.replace(self.path, '').count(os.sep)
            indent = "|\t" * (level - 1)

            if level == 0:
                result += f'{indent}V {os.path.basename(root)}\n'
            else:
                result += f'{indent}|-> V {os.path.basename(root)}\n'

            subindent = "|\t" * level
            for file in files:
                result += f'{subindent}|-> {file}\n'

        return result

    def __contains__(self, item):
        for elements in os.walk(self.path):
            if item in elements[1] + elements[2]:
                return True
        return False


if __name__ == "__main__":
    folder1 = PrintableFolder("E:\\GitHub\\EpamPython2019\\07-python-for-advanced")
    folder2 = PrintableFolder("E:\\GitHub\\EpamPython2019\\06-advanced-python")
    print(folder1)
    print(folder2)
    file1 = "task1.py"
    file2 = "task2.py"
    file3 = "task3.py"
    print(file1 in folder2)
    print(file2 in folder1)
