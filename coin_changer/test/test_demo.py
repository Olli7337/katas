import  unittest

# 0 -> []
# 10 -> [10]
# 20 -> [20]
# 30 -> [20, 10]
# 40 -> [20, 20]

def coin_changer(amount):
    pass
    coins = []
    while amount >= 100:
        coins.append(100)
        amount=amount-100
    while amount >= 50:
        coins.append(50)
        amount=amount-50
    while amount >= 20:
        coins.append(20)
        amount=amount-20
    while amount >= 10:
        coins.append(10)
        amount = amount - 10


    return coins


class MyTest(unittest.TestCase):
    def test_0(self):
        self.assertEqual([], coin_changer(0))
    def test_10(self):
        self.assertEqual([10], coin_changer(10))
        self.assertEqual([20], coin_changer(20))
        self.assertEqual([50], coin_changer(50))
    def test_30(self):
        self.assertEquals([20,10],coin_changer(30))
        self.assertEquals([20,20],coin_changer(40))
        self.assertEquals([100],coin_changer(100))
