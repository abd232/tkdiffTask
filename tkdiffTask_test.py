import unittest
import main

class tkdiffTask_test(unittest.TestCase):

    def test_output(self):
        try:
            f1 = open("expected_outputs/test1_test2_output.txt", "r")
            f2 = open("expected_outputs/test1_test3_output.txt", "r")
            f3 = open("expected_outputs/test2_test3_output.txt", "r")

        except:
            print("some files is messing clone again it from my github https://github.com/abd232/tkdiffTask.git")
            exit(4)

        self.assertAlmostEqual(main.main("filesToTestOn/test1.py", "filesToTestOn/test2.py"), f1.readlines())
        self.assertAlmostEqual(main.main("filesToTestOn/test1.py", "filesToTestOn/test3.py"), f2.readlines())
        self.assertAlmostEqual(main.main("filesToTestOn/test2.py", "filesToTestOn/test3.py"), f3.readlines())
    def test_file_dont_exist(self):
        f3 = open("expected_outputs/test2_test3_output.txt", "r")
        self.assertAlmostEqual(main.main("filesToTestOn/test4.py", "filesToTestOn/test3.py"), f3.readlines())
