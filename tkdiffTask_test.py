import unittest
import main

class tkdiffTask_test(unittest.TestCase):
    def test_output(self):
        try:
            f1 = open("expected_outputs/test1_test2_output.txt", "r")
            f2 = open("expected_outputs/test1_test3_output.txt", "r")
            f3 = open("expected_outputs/test2_test3_output.txt", "r")
            s1 = "".join(f1.readlines())
            s2 = "".join(f2.readlines())
            s3 = "".join(f3.readlines())
            f1.close()
            f2.close()
            f3.close()
            

        except:
            print("some files is messing clone again it from my github https://github.com/abd232/tkdiffTask.git")
            exit(4)
        self.assertTrue(main.main("filesToTestOn/test1.py", "filesToTestOn/test2.py")== s1)
        self.assertTrue(main.main("filesToTestOn/test1.py", "filesToTestOn/test3.py")== s2)
        self.assertTrue(main.main("filesToTestOn/test2.py", "filesToTestOn/test3.py")== s3)
    def test_file_dont_exist(self):
        self.assertTrue(main.main("filesToTestOn/test4.py", "filesToTestOn/test2.py") == "one or both of files does not exist")
