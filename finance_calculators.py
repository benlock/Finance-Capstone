import math

#Offers the user a menu of calculations to choose from
print("Choose either 'investment' or 'bond from the menu below to proceed:")
print()
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")

#Takes the user's answer and converts it to lowercase
calc_type = input().lower()

#Gets the relevant data from the user for an investment
if  calc_type == "investment":
    deposit = int(input("How much are you depositing?"))
    invest_interest = int(input("What is the interest rate?"))/100
    investment_duration = int(input("How many years are you investing for?"))
    interest = input("Do you want simple or compound interest?").lower()

    #Calculates the return on simple interest
    if interest == "simple":
        simple_return = deposit * ((1 + (invest_interest * investment_duration)))
        print(f"Your return will be £{simple_return}")

    #Calculates the return on compound interest
    elif interest == "compound":
        compound_return = deposit * (math.pow((1 + invest_interest), investment_duration))
        print(f"Your return will be {round(compound_return, 2)}")
    
    #Returns an error if the user inputs something other than the allowed types of interest
    else:
        print("Please enter a valid interest type")

#Gets the relevant data from the user for a bond
elif calc_type == "bond":
    present_value = int(input("What is the present value of the house?"))
    monthly_bond_interest = ((int(input("What is the annual interest rate?")))/100)/12
    repay_duration = int(input("How many months do you plan to take to repay the bond?"))

    #Calculates monthly repayments by dividing the total owed by the number of months to repay it
    total_owed = present_value * (1 + (monthly_bond_interest * repay_duration))
    repayment_amount = total_owed / repay_duration

    #Returns monthly bond repayments
    print(f"Your monthly bond repayment will be £{round(repayment_amount, 2)}")

#Returns an error if the user enters an invalid input
else:
    print("Error: Please enter a valid calculation type")
