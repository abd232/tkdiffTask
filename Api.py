import GUI
import Tkdiff


class Api:
    def __init__(self, firstFile, secondFile):
        self.__firstFile = firstFile
        self.__secondFile = secondFile
        self.__gui = GUI.GUI(self.__firstFile, self.__secondFile)
        self.__tkdiff = Tkdiff.Tkdiff(self.__firstFile, self.__secondFile)

    def getDeffer(self):
        return self.__tkdiff.get__differ()

    def printDeffer(self):
        difference = '\n'.join(self.__tkdiff.get__differ())
        print(difference)

    def resetDeffer(self):
        self.__tkdiff.resetDeffer()

    def insertText(self, n, text):
        self.__gui.insertToText(n, text)

    def highLight(self, n, color, start, end):
        self.__gui.highLightText(n, color, start, end)

    def finishAddingToGUI(self):
        self.__gui.mainLoop()
