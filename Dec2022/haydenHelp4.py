cost = float(input("Enter the cost of the item: "))
DownPayment =  0.10 * cost
StartingBalance = cost - DownPayment

for month in range(200):
    print(month + 1)
    MonthlyPayment = cost * .05 
    InterestRate= cost * .12 / 12
    Principal = MonthlyPayment - InterestRate 
    endingBalance = StartingBalance - Principal
    StartingBalance = endingBalance
    print(month, "\t\t", StartingBalance, "\t\t" , InterestRate, "\t\t" , Principal, "\t\t" , MonthlyPayment, "\t\t",  endingBalance)