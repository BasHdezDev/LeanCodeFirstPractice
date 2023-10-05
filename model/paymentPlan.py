from datetime import date, datetime, timedelta
from model.creditCard import CreditCard


class PaymentPlan:
    """
    Represents a payment plan in the system, also **IMPORTANT**
    """
    def __init__(self, card_number, purchase_date, purchase_amount):
        self.card_number: str = card_number
        self.purchase_date: date = purchase_date
        self.purchase_amount: float = purchase_amount
        self.payment_date: date = self.purchase_date
        self.interest_amount: float = 0
        self.capital_amount: float = 0
        self.balance: float = 0
        self.payment_amount: float = 0

