from difflib import Differ


class Tkdiff:
    def __init__(self, firstFile, secondFile):
        self.__firstFile = firstFile
        self.__secondFile = secondFile
        try:
            with open(self.__firstFile) as f:
                file1_lines = f.readlines()
        except:
            raise ValueError("file " + str(self.__firstFile) + " does not exist")
        try:
            with open(self.__secondFil) as f:
                file2_lines = f.readlines()
        except:
            raise ValueError("file " + str(self.__secondFile) + " does not exist")
        self.__d = Differ().compare(file1_lines, file2_lines)

    def get__differ(self):
        return self.__d

    def resetDeffer(self):
        with open(self.__firstFile) as f:
            file1_lines = f.readlines()
        with open(self.__secondFile) as f:
            file2_lines = f.readlines()
        self.__d = Differ().compare(file1_lines, file2_lines)

