import unittest

def add(x,y):
    return x+y

class myapp(unittest.TestCase):
    def test_case_add(self):
        a=12
        b=22
        c=add(a,b)
        self.assertEqual(a+b,c)

    def test_case_add1(self):
        a=12.25
        b=13.45
        c=add(a,b)
        self.assertEqual(a+b,c)

    def test_case_add2(self):
        a=12
        b=-8
        c=add(a,b)
        self.assertEqual(a+b,c)


if __name__=="__main__":
    unittest.main()