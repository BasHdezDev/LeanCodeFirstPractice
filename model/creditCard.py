from datetime import date
import Exceptions


class CreditCard:
    """
    Represents a credit card in the system, this will be used in the whole proyect **IMPORTANT**
    """
    def __init__(self, card_number, owner_id, owner_name, bank_name, due_date, franchise, payment_day, monthly_fee,
                 interest_rate):
        self.card_number: int = card_number
        self.owner_id: int = owner_id
        self.owner_name: str = owner_name
        self.bank_name: str = bank_name
        self.due_date: date = due_date
        self.franchise: str = franchise
        self.payment_day: int = payment_day
        self.monthly_fee: float = monthly_fee
        self.interest_rate: float = interest_rate
        self.ANUALINTEREST = self.interest_rate * 12
        self.interest_percentage = self.interest_rate/100

    def total_interest(self, amount: float, installments: int) -> float:

        """
        Calculates the total interest payment for an installment purchase
        """

        payment_value: float = self.monthly_payment(amount, installments)
        total_interest: float = round((payment_value * installments) - amount, 2)
        return total_interest

    @staticmethod
    def saving_plan(monthly_amount: float, total_amount: float, saving_interest: float) -> float:
        """
        Calculates the number of months that the user should save to make the same
        purchase instead of buying it in installments
        """
        total_interest: float = 0
        subtotal: float = 0
        payment_number: int = 0
        while subtotal < total_amount:
            payment_number += 1
            subtotal += round(monthly_amount + total_interest, 4)
            total_interest = round(saving_interest * subtotal, 4)
            if subtotal >= total_amount:
                return payment_number

    def monthly_payment(self, amount: float, installments: int) -> float:
        """
        Calculates the monthly payment for an installment purchase
        """
        if amount == 0:
            raise Exceptions.ZeroAmount
        elif installments <= 0:
            raise Exceptions.NegativePayments
        if self.interest_rate == 0:
            return amount / installments
        if installments == 1:
            return amount
        else:
            return round((amount * self.interest_percentage)/(1 - (1 + self.interest_percentage)**(-installments)), 4)


