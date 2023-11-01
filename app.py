from datetime import date

from flask import Flask, request, render_template
from model.creditCard import CreditCard
from controller import controllerCreditCard, controllerPaymentPlan

app = Flask(__name__)


@app.route('/params')
def params():
    return request.form


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/api/card/new')
def show():
    return render_template("newcard.html")


@app.route('/api/simulate/purchase')
def show_simulate():
    return render_template("simulatepurchase.html")


@app.route('/api/simulate/saving')
def show_savingplan():
    return render_template("planedsaving.html")


@app.route('/api/purchase/new')
def show_paymentplan():
    return render_template("paymentplan.html")


@app.route('/api/payment/programation')
def show_payment_programation():
    return render_template("payment_programation.html")


"""
R1
"""


@app.route('/api/card/new/login')
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

        return render_template("pass.html")
    except Exception as err:
        return {"status": "error", "mensaje": "La peticion no se puede completar", "error": str(err)}


"""
R2
"""


@app.route('/api/simulate/purchase/logic')
def simulate_purchase():

    try:
        card_number = request.args["card_number"]

        card_search = controllerCreditCard.search_by_id(card_number)
        purchase_amount = float(request.args["purchase_amount"])
        payments = float(request.args["payments"])

        monthly_payment = card_search.monthly_payment(purchase_amount, payments)
        interest = card_search.total_interest(purchase_amount, payments)

        return render_template("pass_simulate.html", m=monthly_payment, i=interest)
    except Exception as err:
        return {"status": "error", "mensaje": "La peticion no se puede completar", "error": str(err)}


"""
R3
"""


@app.route('/api/simulate/saving/logic')
def simulate_planned_saving():

    try:
        purchase_amount = float(request.args["purchase_amount"])
        monthly_payment = int(request.args["monthly_payment"])
        interest_rate = float(request.args["interest_rate"])

        planned_saving = CreditCard.saving_plan(monthly_payment, purchase_amount, interest_rate)

        return render_template("pass_planedsaving.html", m=planned_saving)
    except Exception as err:
        return {"status": "error", "message": "Request could not be completed", "error": str(err)}


"""
R4
"""


@app.route('/api/purchase/new/logic')
def simulate_payment_plan():
    try:
        card_number = request.args["card_number"]
        purchase_amount = float(request.args["purchase_amount"])
        purchase_date = date.fromisoformat(request.args["purchase_date"])
        payments = int(request.args["payments"])

        controllerPaymentPlan.insert(card_number, purchase_amount, purchase_date, payments)

        return render_template("pass.html")

    except Exception as err:
        return {"status": "error", "message": "Request could not be completed", "error": str(err)}


"""
R5
"""


@app.route('/api/card/show')
def showcard():
    try:
        card_number = request.args["card_number"]

        response = controllerCreditCard.search_by_id(card_number)

        return {"status": "ok",
                "card number": f"{response.card_number}",
                "owner id": f"{response.owner_id}",
                "owner name": f"{response.owner_name}",
                "bank name": f"{response.bank_name}",
                "due date": f"{response.due_date}",
                "franchise": f"{response.franchise}",
                "payment day": f"{response.payment_day}",
                "monthly fee": f"{response.monthly_fee}",
                "interest rate": f"{response.interest_rate}"
                }
    except Exception as err:
        return {"status": "error", "mensaje": "La peticion no se puede completar", "error": str(err)}


"""
R6
"""


@app.route('/api/payment/programation/logic')
def payment_programation():
    try:

        first_date = request.args["first_date"]
        last_date = request.args["last_date"]

        amount = controllerPaymentPlan.calc_total_payment_in_x_interval(date.fromisoformat(first_date),
                                                                        date.fromisoformat(last_date))

        return render_template("pass_payment_programation.html", m=amount, first=first_date,
                               last=last_date)
    except Exception as err:
        return {"status": "error", "mensaje": "La peticion no se puede completar", "error": str(err)}


if __name__ == '__main__':
    app.run(debug=True)
