import unittest
from datetime import date

from controller import controllerPaymentPlan
from controller import controllerCreditCard
import testControllerCreditCardR1R2


class TestPaymentReport(unittest.TestCase):
    """Tests for the calc total payment in x interval"""

    # TEST FIXTURES
    # Code that runs before each test

    def setUp(self):
        card_number: str = "556677"
        purchase_date: date = date.fromisoformat("2023-09-22")
        amount: float = 200000
        installments: int = 36
        payment_plan = controllerPaymentPlan.insert(card_number, amount, purchase_date, installments)
        card_number: str = "223344"
        purchase_date: date = date.fromisoformat("2023-09-25")
        amount: float = 850000
        installments: int = 24
        payment_plan = controllerPaymentPlan.insert(card_number, amount, purchase_date, installments)
        card_number: str = "445566"
        purchase_date: date = date.fromisoformat("2023-09-29")
        amount: float = 480000
        installments: int = 48
        payment_plan = controllerPaymentPlan.insert(card_number, amount, purchase_date, installments)
        card_number: str = "445566"
        purchase_date: date = date.fromisoformat("2023-11-17")
        amount: float = 90000
        installments: int = 1
        payment_plan = controllerPaymentPlan.insert(card_number, amount, purchase_date, installments)

    def setUpClass():
        """ Executed at the beginning of all tests """
        print("Invoking setUpClass")
        controllerPaymentPlan.create_table()  # Ensure that at the beginning of the tests, the table is created
        controllerCreditCard.delete_all_rows()
        print("Invoking setUpClass")
        controllerCreditCard.create_table()
        tests_credit_cards = testControllerCreditCardR1R2.TestControllerCreditCard()
        tests_credit_cards.test_01_insert1()
        tests_credit_cards.test_01_insert2()
        tests_credit_cards.test_01_insert4()
        tests_credit_cards.test_01_insert5()

    def tearDownClass():
        """ Executed at the end of all tests """
        print("Invoking tearDownClass")
        controllerCreditCard.delete_all_rows()
        controllerPaymentPlan.delete_all_rows()

    def test_05_report_1(self):

        initial_date: date = date.fromisoformat("2023-10-01")
        final_date: date = date.fromisoformat("2023-10-31")

        total: float = controllerPaymentPlan.calc_total_payment_in_x_interval(initial_date, final_date)
        expected: float = 71675
        controllerPaymentPlan.delete_all_rows()

        self.assertEqual(total, expected)

    def test_05_report_2(self):

        initial_date: date = date.fromisoformat("2023-10-01")
        final_date: date = date.fromisoformat("2023-12-31")

        total: float = controllerPaymentPlan.calc_total_payment_in_x_interval(initial_date, final_date)
        expected: float = 305026
        controllerPaymentPlan.delete_all_rows()

        self.assertEqual(total, expected)

    def test_05_report_3(self):

        initial_date: date = date.fromisoformat("2026-01-01")
        final_date: date = date.fromisoformat("2026-12-31")

        total: float = controllerPaymentPlan.calc_total_payment_in_x_interval(initial_date, final_date)
        expected: float = 203682
        controllerPaymentPlan.delete_all_rows()

        self.assertEqual(total, expected)
