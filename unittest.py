import unittest

class Testmyapp2(unittest.TestCase):
    def test_case3(self):
        self.assertEqual("hello","hello")
       # pass
class Testmyapp(unittest.TestCase):
    def test_case1(self):
        a=10
        b=20
        c=a+b
        self.assertEqual(a+b,c)
       # pass
    def test_case2(self):
        self.assertNotEqual("hello","hai")
       # pass



if __name__=="__main__":
    unittest.main()
