import math

print("\nInvestment - to calculate the amount of interest you'll earn on your investment")
print("Bond       - to calculate the amount you'll have to pay on a home loan")

user_choice = input("\n\nPlease select an option by typing either 'investment' or 'bond': ")
user_choice = user_choice.lower() # converts the text to lowercase to meet the requirements for the following if statements

if user_choice == "investment":
    investment_type = input("Select an investment type by typing either 'simple' or 'compound'")
    investment_type = investment_type.lower() # converts the user input to lowercase to meet requirements for the following if statements
    
    if investment_type == "simple":
        user_deposit = float(input("Enter the amount you would like to deposit: ")) #uses float to get the most accurate amount
        years = int(input("Enter the amount of years you would like to invest for: "))
        interest_rate = int(input("Enter the interest rate percentage: "))

        interest_rate = interest_rate/100 # interest rate is whatever the user inputs divided by 100 to get the percentage
        simple_interest_total = user_deposit * (1 + interest_rate * years) # Formula to calculate simple interest rate and add it to the total deposited
        simple_interest_total = float(simple_interest_total)

        years = str(years) #converts to a string for the print statement
        user_deposit = str(user_deposit) #converts to a string for the print statement
        interest_rate = interest_rate*100 #converts the percentage back into the whole number for interest rate
        interest_rate = str(interest_rate) #converts into string for the print statement
        rounded_simple_interest_total = round(simple_interest_total, 2) #rounds the total amount to the nearest 2 decimal places (for pennies)
        string_rounded_simple_interest_total = str(rounded_simple_interest_total)
        
        print("\nTotal invested: £" + user_deposit + "\nTotal years invested: " + years + "\nInterest rate: " + interest_rate + "%" + "\nFinal amount: £" + string_rounded_simple_interest_total)
        

    elif investment_type == "compound":
        user_deposit = float(input("Enter the amount you would like to deposit: "))
        years = int(input("Enter the amount of years you would like to invest for: "))
        interest_rate = int(input("Enter the interest rate percentage: "))
        interest_rate = float(interest_rate/100)

        compound_interest_total = user_deposit * math.pow((1+interest_rate), years) # Formula to calculate the total amount after compound interest
        rounded_total = round(compound_interest_total, 2) #rounds the total to nearest 2 decimal places to account for pennies
        string_rounded_total = str(rounded_total)
        years = str(years)
        user_deposit = str(user_deposit)
        interest_rate = interest_rate*100
        interest_rate = str(interest_rate)

        print("\nTotal invested: £" + user_deposit + "\nTotal years invested: " + years + "\nInterest rate: " + interest_rate + "%" + "\nFinal amount: £" + string_rounded_total)
   

elif user_choice == "bond":
    bond = float(input("Enter value of your house: "))
    interest_rate = int(input("Enter the interest rate percentage: "))
    months = int(input("Enter the amount of months you wish to repay the bond: "))

    interest_rate = interest_rate/100
    interest_rate = interest_rate/12
    repayment = (interest_rate * bond)/(1 - (1 + interest_rate)**(-months)) # Formula to work out the repayment amount of the bond
    repayment = round(repayment, 2) # Amount rounded to nearest 2 decimal places to account for pennies

    string_repayment = str(repayment)
    bond = str(bond)
    interest_rate = interest_rate*12 
    interest_rate = interest_rate*100
    interest_rate = str(interest_rate)
    months = str(months)

    print("\nValue of house: £" + bond + "\nTotal months to repay: " + months + "\nInterest rate: " + interest_rate + "%" + "\nTotal monthly repayment: £" + string_repayment)
    

else:
    print("Incorrect entry") #if user doesn't enter either investment or bond

    





