import  unittest

def largestnumber(x,y):
    if x>y:
        return True
    else:
        return False

class Largestapp(unittest.TestCase):
    def test_case_largest1(self):
        a=20
        b=10
        c=largestnumber(a,b)
        self.assertTrue(c)

    def test_case_largest2(self):
        a=10
        b=20
        c=largestnumber(a,b)
        self.assertFalse(c)


if __name__=="__main__":
    unittest.main()
