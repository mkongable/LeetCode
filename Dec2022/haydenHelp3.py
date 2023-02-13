cost = float(input("Enter the cost of the item: "))

def interest(cost):
    DownPayment =  0.10 * cost
    StartingBalance = cost - DownPayment

    print("Month", "\t\t", "Starting Balance", "\t\t" , "Interest to Pay", "\t\t" , "Principal to Pay", "\t\t" , "Payment", "\t\t",  "Ending Balance")
    month = 1
    while StartingBalance > 0:
        MonthlyPayment = (cost - DownPayment) * .05 # constant payment, doesn't change until the last month
        InterestRate = StartingBalance * .12 / 12 # determined by using current balance and interest rate
        if(StartingBalance < MonthlyPayment):
            MonthlyPayment = StartingBalance
            InterestRate = 0 # if the balance is less than the monthly payment, there is no interest to pay
        Principal = MonthlyPayment - InterestRate
        endingBalance = StartingBalance - Principal
        print(month, "\t\t", "%.2f" % StartingBalance, "\t\t" , "%.2f" %  InterestRate, "\t\t" , "%.2f" % Principal, "\t\t" , "%.2f" % MonthlyPayment, "\t\t", "%.2f" % endingBalance)
        StartingBalance = endingBalance # set the starting balance to the ending balance
        month += 1
        
interest(cost)
