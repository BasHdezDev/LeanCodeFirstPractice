import unittest
from datetime import date

from model.creditCard import CreditCard


class TestPlannedSaving(unittest.TestCase):

    def test_03_savings1(self):
        amount: float = 200000
        interest_rate: float = 0.90
        monthly_amount: float = 6528.817139

        result = CreditCard.saving_plan(monthly_amount, amount, interest_rate)
        expected = 6
        self.assertEqual(result, expected)

    def test_03_savings2(self):
        amount: float = 850000
        interest_rate: float = 0.90
        monthly_amount: float = 39537.78219
        result = CreditCard.saving_plan(monthly_amount, amount, interest_rate)
        expected = 5
        self.assertEqual(result, expected)

    def test_03_savings3(self):
        amount: float = 480000
        interest_rate: float = 0.90
        monthly_amount: float = 10000
        result = CreditCard.saving_plan(monthly_amount, amount, interest_rate)
        expected = 6
        self.assertEqual(result, expected)

    def test_03_planned_saving_4(self):
        amount: float = 90000
        interest_rate: float = 0.90
        monthly_amount: float = 90000
        result = CreditCard.saving_plan(monthly_amount, amount, interest_rate)
        expected = 1
        self.assertEqual(result, expected)
