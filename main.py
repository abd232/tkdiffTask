import Api
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='tkdiff task')
    requiredNamed = parser.add_argument_group('required named arguments')
    requiredNamed.add_argument('-f', '--firstFile', type=str, metavar='', required=True, help='First file name or path')
    requiredNamed.add_argument('-s', '--secondFile', type=str, metavar='', required=True,
                               help='Second file name or path')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--glu', action='store_true', help='print with out glu')
    args = parser.parse_args()
    api = Api.Api(args.firstFile, args.secondFile)
    diff = api.run(not args.glu, True)

else:
    if __name__ == 'tkdiffTask_test':
        def __init__(self, firstFile, secondFile):
            self.__firstFile = firstFile
            self.__secondFile = secondFile
            api = Api.Api(self.__firstFile,self.__secondFile)
            diff = api.run(gui=False,print=False)
            return diff
    else:
        print("https://www.youtube.com/watch?v=bgJ_1WuhUig")
        exit(-1)

