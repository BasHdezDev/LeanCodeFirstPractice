class ZeroAmount(Exception):
    print("The amount must be greater than zero")


class NegativePayments(Exception):
    print("The number of installments must be greater than zero")


class NoCard(Exception):
    print("The indicated card does not exist")


class CreditCardAlreadyInDatabase(Exception):
    print("The credit card already exists")

