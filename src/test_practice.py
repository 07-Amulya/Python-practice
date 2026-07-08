"""
import unittest

def add(a, b):
    return a + b

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

if __name__ == "__main__":
    unittest.main()





import unittest

def multiply(a, b):
    return a * b

class TestMath(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(4, 5), 25)

if __name__ == "__main__":
    unittest.main()





import unittest

class TestNumbers(unittest.TestCase):

    def test_one(self):
        self.assertTrue(5 > 2)

    def test_two(self):
        self.assertFalse(10 < 5)

    def test_three(self):
        self.assertEqual(3 * 4, 12)

if __name__ == "__main__":
    unittest.main()






import unittest

class TestStrings(unittest.TestCase):

    def test_word(self):
        self.assertIn("cat", "concatenate")

if __name__ == "__main__":
    unittest.main()





import unittest

class TestList(unittest.TestCase):

    def setUp(self):
        self.data = [10, 20, 30]

    def test_length(self):
        self.assertEqual(len(self.data), 3)

    def test_sum(self):
        self.assertEqual(sum(self.data), 60)

if __name__ == "__main__":
    unittest.main()





import unittest

def divide(a, b):
    return a / b

class TestDivision(unittest.TestCase):

    def test_error(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

if __name__ == "__main__":
    unittest.main()




import unittest

class Bank:

    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient Balance"
        self.balance -= amount
        return self.balance

class TestBank(unittest.TestCase):

    def test_withdraw(self):
        account = Bank(1000)
        self.assertEqual(account.withdraw(300), 700)

    def test_insufficient(self):
        account = Bank(500)
        self.assertEqual(
            account.withdraw(800),
            "Insufficient Balance"
        )

if __name__ == "__main__":
    unittest.main()





import unittest

class TestDemo(unittest.TestCase):

    def setUp(self):
        print("Setup")

    def tearDown(self):
        print("Teardown")

    def test_one(self):
        print("Test One")

    def test_two(self):
        print("Test Two")

if __name__ == "__main__":
    unittest.main()




import unittest

class TestExample(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Start")

    @classmethod
    def tearDownClass(cls):
        print("End")

    def setUp(self):
        print("Before")

    def tearDown(self):
        print("After")

    def test_first(self):
        print("First")

    def test_second(self):
        print("Second")

if __name__ == "__main__":
    unittest.main()
"""