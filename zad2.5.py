import unittest

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Niepoprawna kwota wpłaty")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Niepoprawna kwota wypłaty")
        if amount > self.balance:
            raise ValueError("Brak środków")
        self.balance -= amount

    def get_balance(self):
        return self.balance


class TestBankAccount(unittest.TestCase):
    def test_deposit(self):
        acc = BankAccount()
        acc.deposit(100)
        self.assertEqual(acc.get_balance(), 100)

    def test_withdraw(self):
        acc = BankAccount(100)
        acc.withdraw(40)
        self.assertEqual(acc.get_balance(), 60)

    def test_invalid_deposit(self):
        acc = BankAccount()
        with self.assertRaises(ValueError):
            acc.deposit(0)

    def test_invalid_withdraw_amount(self):
        acc = BankAccount(100)
        with self.assertRaises(ValueError):
            acc.withdraw(-5)

    def test_invalid_withdraw_too_much(self):
        acc = BankAccount(50)
        with self.assertRaises(ValueError):
            acc.withdraw(100)


if __name__ == "__main__":
    unittest.main(verbosity=2)
