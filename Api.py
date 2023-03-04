import GUI
import Tkdiff


class Api:
    def __init__(self, firstFile, secondFile):
        self.__firstFile = firstFile
        self.__secondFile = secondFile
        self.__gui = GUI.GUI(self.__firstFile, self.__secondFile)
        self.__tkdiff = Tkdiff.Tkdiff(self.__firstFile, self.__secondFile)
    def run(self,gui,print):
        difference = '\n'.join(self.__tkdiff.get__differ())
        if print:
            print(difference)
        self.__tkdiff.resetDeffer()
        d = self.__tkdiff.get__differ()
        try:
            r = next(d)
            no_empty_file = True
        except StopIteration:
            no_empty_file = False
        flag = False
        next_in_r2 = False
        f1_line_counter = 1
        f2_line_counter = 1
        while no_empty_file:
            if r[0] == ' ':
                self.__gui.add_green_text(0, r[2::], ''.join((str(f1_line_counter), ".0")),
                                             ''.join((str(f1_line_counter + 1), ".0")))
                self.__gui.add_green_text(1,  r[2::], ''.join((str(f2_line_counter), ".0")),
                                             ''.join((str(f2_line_counter + 1), ".0")))
                #print("line: '" + r[2:len(r)-1]+"' from line " + str(f1_line_counter) + " in " + self.__firstFile +
                      #" and line " + str(f1_line_counter) +" in " + self.__secondFile +"stayed the same")
                f1_line_counter = f1_line_counter + 1
                f2_line_counter = f2_line_counter + 1
                flag = True
            else:
                try:
                    if next_in_r2:
                        r1 = r2
                        next_in_r2 = False
                    else:
                        r1 = next(d)
                    flag = False
                    if r1[0] != '?':
                        if r[0] == '-':
                            try:
                                r2 = next(d)
                                next_in_r2 = True
                                if r2[0] == '?':
                                    self.__gui.add_yellow_text(0, r[2::], ''.join((str(f1_line_counter), ".0")),
                                                               ''.join((str(f1_line_counter + 1), ".0")))
                                    #print("line: '" + r[2:len(r)-1] + "' from line " + str(f1_line_counter) + "have small changes.")
                                    f1_line_counter = f1_line_counter + 1
                                else:
                                    self.__gui.add_red_text(0, r[2::], ''.join((str(f1_line_counter), ".0")),
                                                            ''.join((str(f1_line_counter + 1), ".0")))
                                    f1_line_counter = f1_line_counter + 1
                            except StopIteration:
                                self.__gui.add_red_text(0, r[2::], ''.join((str(f1_line_counter), ".0")),
                                                        ''.join((str(f1_line_counter + 1), ".0")))
                                f1_line_counter = f1_line_counter + 1
                        else:
                            self.__gui.add_blue_text(1, r[2::], ''.join((str(f2_line_counter), ".0")),
                                                    ''.join((str(f2_line_counter + 1), ".0")))

                            f2_line_counter = f2_line_counter + 1
                        r = r1
                    else:
                        if r[0] == '-':
                            self.__gui.add_yellow_text(0, r[2::], ''.join((str(f1_line_counter), ".0")),
                                                       ''.join((str(f1_line_counter + 1), ".0")))
                            #print("line: '" + r[2:len(r)-1] + "' from line " + str(f1_line_counter) + "have small changes.")
                            f1_line_counter = f1_line_counter + 1
                        else:
                            self.__gui.add_yellow_text(1, r[2::], ''.join((str(f2_line_counter), ".0")),
                                                       ''.join((str(f2_line_counter + 1), ".0")))
                            f2_line_counter = f2_line_counter + 1
                        k = 2
                        l = 0
                        for i in r1[2::]:
                            k = l
                            if i == '+':
                                if r[0] == '-':
                                    self.__gui.highLightText(0, "blue", ''.join((str(f1_line_counter - 1), ".", str(k))),
                                                         ''.join((str(f1_line_counter - 1), ".", str(k + 1))))
                                else:
                                    self.__gui.highLightText(1, "blue", ''.join((str(f2_line_counter - 1), ".", str(k))),
                                                             ''.join((str(f2_line_counter - 1), ".", str(k + 1))))
                            if i == '-':
                                if r[0] == '-':
                                    self.__gui.highLightText(0, "red", ''.join((str(f1_line_counter - 1), ".", str(k))),
                                                             ''.join((str(f1_line_counter - 1), ".", str(k + 1))))
                                else:
                                    self.__gui.highLightText(1, "red", ''.join((str(f2_line_counter - 1), ".", str(k))),
                                                             ''.join((str(f2_line_counter - 1), ".", str(k + 1))))
                            if i == '^':
                                if r[0] == '-':
                                    self.__gui.highLightText(0, "orange", ''.join((str(f1_line_counter - 1), ".", str(k))),
                                                             ''.join((str(f1_line_counter - 1), ".", str(k + 1))))
                                else:
                                    self.__gui.highLightText(1, "orange", ''.join((str(f2_line_counter - 1), ".", str(k))),
                                                             ''.join((str(f2_line_counter - 1), ".", str(k + 1))))
                            l = l + 1
                        r = next(d)

                except StopIteration:
                    break
            if flag:
                try:
                    r = next(d)
                except StopIteration:
                    break
        if gui:
            self.__gui.mainLoop()
        self.__tkdiff.resetDeffer()
        difference = '\n'.join(self.__tkdiff.get__differ())
        return difference


    def printDeffer(self):
        difference = '\n'.join(self.__tkdiff.get__differ())
        print(difference)

    def insertText(self, n, text):
        self.__gui.insertToText(n, text)

    def highLight(self, n, color, start, end):
        self.__gui.highLightText(n, color, start, end)

