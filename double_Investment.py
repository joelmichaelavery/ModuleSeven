#Joel Avery 
#Module 7 Assignment 
#11/18/22

#This program takes the input of annualized interest rate, and the 
# initial investment amount and loops over until the the amount is #doubled, 
#and then takes the number of years that it took to double. 

#Takes the input from the user for initial investment
initial_investment = input("Please enter an initial investment amount : ")

#Takes the input from the user for annual rate as a whole number
annual_rate = input("Please enter an annual rate as a whole number: ")

#Changes type of the initial_investment to a float
initial_investment = float(initial_investment)

#Changes the type of the annual rate to a float, divided by 100 and stored as 
#a float. 
annual_rate = float(float(annual_rate)/100)

#begin with year being year 1
year = 1

#variable year_end_balance to have the first year end total. 
year_end_balance = (initial_investment * annual_rate) + initial_investment

#do not want the first year in the while loop, so start with year end balance
#for year one, and format using f string, and to two decimals. 
print(f"After {year} year, your balance is {year_end_balance:.{2}f}!\n")

#flag to enter the while loop and stay until it turns false. 
investment_active = True

#while loop to check the flag. 
while investment_active:
    year += 1 #increment the year variable every iteration. 

    #continues with year end balance. 
    year_end_balance = (year_end_balance * annual_rate) + year_end_balance

    #outputs a nicely formatted end of year balance to two decimals. 
    print(f"After {year} year, your balance is {year_end_balance:.{2}f}!\n")

    #conditional statement to check if the year end balance is double the 
    #initial investment
    if ((year_end_balance) / (initial_investment)) >= 2:
        print(f"It took {year} years to double!") #output the time it took to double
        #if this condition happens, it changes the flag to False, and loop ends. 
        investment_active = False

