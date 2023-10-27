from datetime import date

from flask import Flask, request
from model.creditCard import CreditCard
from controller import controllerCreditCard, controllerPaymentPlan

app = Flask(__name__)


@app.route('/params')
def params():
    return request.args


"""
R1
Usage example
http://127.0.0.1:5000/api/card/new?card_number=1256487&owner_id=1255487896&owner_name=DonJules&bank_name=Falabella&due_date=2028-10-25&franchise=VISA&payment_day=10&monthly_fee=24000&interest_rate=3.1
"""


@app.route('/api/card/new')
def createcard():
    try:
        card_number = request.args["card_number"]
        owner_id = request.args["owner_id"]
        owner_name = request.args["owner_name"]
        bank_name = request.args["bank_name"]
        due_date = request.args["due_date"]
        franchise = request.args["franchise"]
        payment_day = int(request.args["payment_day"])
        monthly_fee = int(request.args["monthly_fee"])
        interest_rate = float(request.args["interest_rate"])

        creditcard_test = CreditCard(card_number, owner_id, owner_name, bank_name, due_date, franchise, payment_day,
                                     monthly_fee, interest_rate)

        controllerCreditCard.insert(creditcard_test)

        return {"status": "ok"}
    except Exception as err:
        return {"status": "error", "mensaje": "La peticion no se puede completar", "error": str(err)}


"""
R2
http://127.0.0.1:5000/api/simulate/purchase?card_number=1256487&purchase_amount=480000&payments=48
"""


@app.route('/api/simulate/purchase')
def simulate_purchase():

    try:
        card_number = request.args["card_number"]

        card_search = controllerCreditCard.search_by_id(card_number)
        purchase_amount = float(request.args["purchase_amount"])
        payments = float(request.args["payments"])

        monthly_payment = card_search.monthly_payment(purchase_amount, payments)
        interest = card_search.total_interest(purchase_amount, payments)

        return {"status": "ok", "monthly_payment": f"{monthly_payment}", "total_interest": f"{interest}"}
    except Exception as err:
        return {"status": "error", "mensaje": "La peticion no se puede completar", "error": str(err)}


"""
R3
http://127.0.0.1:5000/api/simulate/saving?card_number=1256487&purchase_amount=480000&payments=24
"""


@app.route('/api/simulate/saving')
def simulate_planned_saving():

    try:
        purchase_amount = float(request.args["purchase_amount"])
        monthly_payment = int(request.args["monthly_payment"])
        interest_rate = float(request.args["interest_rate"])

        planned_saving = CreditCard.saving_plan(monthly_payment, purchase_amount, interest_rate)

        return {"status": "ok", "months": planned_saving}
    except Exception as err:
        return {"status": "error", "message": "Request could not be completed", "error": str(err)}


"""
R4
/api/purchase/new?card_number=1256487&purchase_amount=200000&&payments=36&purchase_date=2023-09-11
"""


@app.route('/api/purchase/new')
def simulate_payment_plan():
    try:
        card_number = request.args["card_number"]
        purchase_amount = float(request.args["purchase_amount"])
        purchase_date = date.fromisoformat(request.args["purchase_date"])
        payments = int(request.args["payments"])

        controllerPaymentPlan.insert(card_number, purchase_amount, purchase_date, payments)

        return {"status": "ok"}

    except Exception as err:
        return {"status": "error",
                "message": "Request could not be completed",
                "error": str(err)}


if __name__ == '__main__':
    app.run(debug=True)
