import Api
import argparse
parser = argparse.ArgumentParser(description='tkdiff task')
requiredNamed = parser.add_argument_group('required named arguments')
requiredNamed.add_argument('-f', '--firstFile', type=str, metavar='', required=True, help='First file name or path')
requiredNamed.add_argument('-s', '--secondFile', type=str, metavar='', required=True, help='Second file name or path')
group = parser.add_mutually_exclusive_group()
group.add_argument('--glu', action='store_true', help='print with out glu')
args = parser.parse_args()
if __name__ == '__main__':
    api = Api.Api(args.firstFile, args.secondFile)
    api.printDeffer()
    if not args.glu:
        api.resetDeffer()
        d = api.getDeffer()

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
                api.insertText(0, r[2::])
                api.highLight(0,"green", ''.join((str(f1_line_counter), ".0")), ''.join((str(f1_line_counter + 1)
                                                                                         , ".0")))
                f1_line_counter = f1_line_counter + 1
                api.insertText(1, r[2::])
                api.highLight(1, "green", ''.join((str(f2_line_counter), ".0")), ''.join((str(f2_line_counter + 1), ".0")))
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
                                    api.insertText(0, r[2::])
                                    api.highLight(0, "yellow", ''.join((str(f1_line_counter), ".0")),
                                                  ''.join((str(f1_line_counter + 1), ".0")))
                                    f1_line_counter = f1_line_counter + 1
                                else:

                                    api.insertText(0, r[2::])
                                    api.highLight(0, "red", ''.join((str(f1_line_counter), ".0")),
                                                  ''.join((str(f1_line_counter + 1), ".0")))
                                    f1_line_counter = f1_line_counter + 1
                            except StopIteration:
                                api.insertText(0, r[2::])
                                api.highLight(0, "red", ''.join((str(f1_line_counter), ".0")),
                                              ''.join((str(f1_line_counter + 1), ".0")))
                                f1_line_counter = f1_line_counter + 1
                        else:
                            api.insertText(1, r[2::])
                            api.highLight(1, "blue", ''.join((str(f2_line_counter), ".0")),
                                          ''.join((str(f2_line_counter + 1), ".0")))
                            f2_line_counter = f2_line_counter + 1
                        r = r1
                    else:
                        if r[0] == '-':
                            api.insertText(0, r[2::])
                            api.highLight(0, "yellow", ''.join((str(f1_line_counter), ".0")),
                                          ''.join((str(f1_line_counter + 1), ".0")))
                            f1_line_counter = f1_line_counter + 1
                        else:
                            api.insertText(1, r[2::])
                            api.highLight(1, "yellow", ''.join((str(f2_line_counter), ".0")),
                                          ''.join((str(f2_line_counter + 1), ".0")))
                            f2_line_counter = f2_line_counter + 1
                        k = 2
                        l = 0
                        for i in r1[2::]:
                            k = l
                            if i == '+':
                                if r[0] == '-':
                                    api.highLight(0, "blue", ''.join((str(f1_line_counter - 1), ".", str(k))),
                                                  ''.join((str(f1_line_counter - 1), ".", str(k + 1))))
                                else:
                                    api.highLight(1, "blue", ''.join((str(f2_line_counter - 1), ".", str(k))),
                                                  ''.join((str(f2_line_counter - 1), ".", str(k + 1))))
                            if i == '-':
                                if r[0] == '-':
                                    api.highLight(0, "red", ''.join((str(f1_line_counter - 1), ".", str(k))),
                                                  ''.join((str(f1_line_counter - 1), ".", str(k + 1))))
                                else:
                                    api.highLight(1, "red", ''.join((str(f2_line_counter - 1), ".", str(k))),
                                                  ''.join((str(f2_line_counter - 1), ".", str(k + 1))))
                            if i == '^':
                                if r[0] == '-':
                                    api.highLight(0, "orange", ''.join((str(f1_line_counter - 1), ".", str(k))),
                                                  ''.join((str(f1_line_counter - 1), ".", str(k + 1))))
                                else:
                                    api.highLight(1, "orange", ''.join((str(f2_line_counter - 1), ".", str(k))),
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
        api.finishAddingToGUI()

