import unittest
def add(a, b):
 return a + b


class SumTest(unittest.TestCase):

     def test_sumfunc_1(self):#assign
      a=10
      b=20
      result = sum(a,b)

      self.assertEqual(result , a+b)#assert



     def test_sumfunc_2(self):
      a=10
      b=20
      result = sum(b,a)

      self.assertEqual(result , a+b)

if __name__ == "__main__":
    unittest.main 
