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
    api = Api.Api(args.firstFile[2::], args.secondFile[2::])
    diff = api.run(not args.glu, True)
    if diff == "one or both of files does not exist":
    	print("one or both of files does not exist")

else:
    if not (__name__ == 'main'):
        print("https://www.youtube.com/watch?v=bgJ_1WuhUig")
        exit(-1)
def main(firstFile, secondFile):
    api = Api.Api(firstFile,secondFile)
    diff = api.run(gui=False,printt=False)
    return diff
