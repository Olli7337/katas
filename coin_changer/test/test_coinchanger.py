import unittest

# Specs
# Change (5) -> [5]
# Change (110) -> [100,10]
# Change (340) -> [200,100,20,20]



def change(x):
    result = []
    if  (x > 10):
        result.append(10)
        x = x-10
    result.append(x)

    return result

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual([5], change(5))

    def test_10(self):
        self.assertEqual([10], change(10))
    def test_15(self):
        self.assertEqual([10, 5], change(15))
