outstandingBalance = float(raw_input('Enter the outstanding balance on your credit card: '))
annualInterestRate = float(raw_input('Enter the annual interest rate as a decimal: '))
""" Calculates the minimum fixed monthly payment needed in order to pay off credit card balance within
    12 months. Not Dealing with a minimum monthly payment rate."""

minMonthlyPayment = 0
monthlyInterestRate = annualInterestRate/12
balance = outstandingBalance

while balance > 0:
    balance = outstandingBalance
    month = 0
    minMonthlyPayment += 10

    while balance > 0 and month < 12:
        balance = balance*(1+monthlyInterestRate) -  minMonthlyPayment
        month += 1
        balance = round(balance, 2)
    
print 'RESULT'
print 'Monthly payment to pay off debt in  1 year: ' , minMonthlyPayment
print 'Number of months needed: ', month
print 'Balance: ', balance


