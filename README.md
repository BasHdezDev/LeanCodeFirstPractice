# Creditcard Software

Main Software of credit cards handling using Lean Code principles and TDD methodologies

Sample using MVC pattern bound to postgresql
also used Spring Boot Project Architecture:


![image](https://github.com/BasHdezDev/Quotes/assets/109814105/dd799183-27f8-424e-92ea-da2e39dde22f)

Postgresql Database used on neon.tech

The double t in inittial commit, just forget it ahhahaha

by Sebastián Hernández Díaz


# How To Use the Software
- First get an account in neon.tech and sign up
- Create a project, give it whatever name you want
- When you are in your project, go to dashboard
- In that page, you will see a blurred part in a code, click on it and then it would be a non-blurred text, that's your password, be careful
- Then, in the part that says 'psql', click on it, and the choose Django
- You will see something like this:
  
- DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'neondb',
    'USER': 'YOURUSER',
    'PASSWORD': 'YOURPASSWORD',
    'HOST': 'YOURHOST',
    'PORT': 'YOURPORT',
  }
}

- Then, go to the file Secret_Config-sample.py and refactor it as Secret_Config.py
- Then, in the code you will change the things as the following instructions:


- In DATABASE = "You will write what it says on NAME"
- In USER = "You will write what it says on USER"
- In PASSWORD = "You will write what it says on PASSWORD"
- In HOST = "ou will write what it says on HOST"
- In PORT = 5432  # BY DEFAULT IT IS 5432, BUT IT CAN CHANGE IN YOUR DB


# How to run the web service

- After get done the software configuration right above, click on app.py and see the whole file
- Run it and in the terminal, it would create a link (Normally this one: **http://127.0.0.1:5000**)
- Click on it and open it in your browser (**Please do it on Chrome**)
- When you enter on the page, you will see a **Not Found ERROR**, Don't be afraid, its normal!
- In the app.py you will see a comment between """ **TEXT_HERE** """, in that comment, you will find a R1, R2, R3, R4, and right below a function
- The function will always start with **@app.route('*/HERE_GOES_A_WEB_ROUTE*')**


**----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------**
  
- ## For the R1:
- You must provide a:
- card_number = XXXXXXXXXX    **Insert a card number** *Normally a number*
- owner_id = XXXXXXXXX        **Insert an ID** *Normally a number*
- owner_name = XXXXXXXXX      **Insert a name**
- bank_name = XXXXXXXXX       **Insert the name of the bank where belong the credit card**
- due_date = YYYY-MM-DD       **Insert the due date of the credit card in this way *YEAR-MONTH-DAY***
- franchise = XXXXXXXX        **Insert the franchise of the credit card**
- payment_day = DD            **Insert the payment day of the credit card in this way *DAY*** *Normally a number*
- monthly_fee = XXXXXXX       **Insert the monthly fee of the credit card** *Normally a number*
- interest_rate = XXXXX       **Insert the interest rate** *Normally a number*

- After put everything in his place, you will put it in the next path:

- http://127.0.0.1:5000/api/card/new?card_number=YOUR_CARD_NUMBER&owner_id=YOUR_OWNER_ID&owner_name=YOUR_OWNER_NAME&bank_name=YOUR_BANK_NAME&due_date=YOUR_DUE_DATE&franchise=YOUR_FRANCHISE&payment_day=YOUR_PAYMENT_DAY&monthly_fee=YOUR_MONTHLY_FEE&interest_rate=YOUR_INTEREST_RATE

Copy the whole path and copy it on the search bar and click enter

**----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------**

- ## For the R2:
- You must provide a:
- card_number = XXXXXXXXXX       **Insert a card number that you already registered in the database** **If the card number does'nt exists in the database it would show an error** *Normally a number*
- purchase_amount = XXXXXXXXX    **Insert a purchase amount** *Normally a number*
- payments = XXXXXXXXX           **Insert how many payments you will do** *Normally a number*


- After put everything in his place, you will put it in the next path:

- http://127.0.0.1:5000/api/simulate/purchase?card_number=YOUR_CARD_NUMBER&purchase_amount=THE_PURCHASE_AMOUNT&payments=YOUR_NUMBER_OF_PAYMENTS

Copy the whole path and copy it on the search bar and click enter

**---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------**

- ## For the R3:
- You must provide a:
- purchase_amount = XXXXXXXXXX    **Insert a purchase amount** *Normally a number*
- monthly_payment = XXXXXXXXX     **Insert a monthly payment** *Normally a number*
- interest_rate = XXXXX           **Insert the interest rate** *Normally a number*

- After put everything in his place, you will put it in the next path:

- http://127.0.0.1:5000/api/simulate/saving?card_number=YOUR_CARD_NUMBER&purchase_amount=YOUR_PURCHASE_AMOUNT&payments=YOUR_NUMBER_OF_PAYMENTS

Copy the whole path and copy it on the search bar and click enter


**---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------**

- ## For the R4:
- You must provide a:
- card_number = XXXXXXXXXX        **Insert a card number that you already registered in the database** **If the card number does'nt exists in the database it would show an error** *Normally a number*
- purchase_amount = XXXXXXXXXX    **Insert a purchase amount** *Normally a number*
- purchase_date = YYYY-MM-DD      **Insert the due date of the credit card in this way *YEAR-MONTH-DAY***
- payments = XXXXXXXXX           **Insert how many payments you will do** *Normally a number*

- After put everything in his place, you will put it in the next path:

- http://127.0.0.1:5000/api/purchase/new?card_number=YOUR_CARD_NUMBER&purchase_amount=YOUR_PURCHASE_AMOUNT&&payments=NUMBER_OF_PAYMENTS&purchase_date=YOUR_PURCHASE_DATE

Copy the whole path and copy it on the search bar and click enter

**---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------**

- ## For the R5:
- You must provide a:
- card_number = XXXXXXXXXX        **Insert a card number that you already registered in the database** **If the card number does'nt exists in the database it would show an error** *Normally a number*

- After put everything in his place, you will put it in the next path:

- http://127.0.0.1:5000/api/card/show?card_number=YOUR_CREDIT_CARD

Copy the whole path and copy it on the search bar and click enter
