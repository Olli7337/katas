import unittest

# Specs
# Change (5) -> [5]
# Change (110) -> [100,10]
# Change (340) -> [200,100,20,20]



def change(x):
    return [5]

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual([5], change(5))