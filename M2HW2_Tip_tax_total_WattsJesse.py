# CTI-110 
# M2HW1-Tips, tax, & total
# Jesse Watts
# 17 Sep 17
# Calculate the total cost of a meal incl. tip & tax

# Declare variables
foodCost = float(input('Enter the cost of food: $'))
tax = foodCost * 0.07
subTotal = foodCost + tax
tipAmount = subTotal * 0.18
totalCost = subTotal + tipAmount

# Calculate the tax at 7%
tax = foodCost * 0.07
tax = (100.00*0.07)

# Calculate the subTotal
subTotal = foodCost + tax
subTotal = 100.00 + 7.00

# Calculate the tipAmount
tipAmount = subTotal * 0.18
tipAmount = 107.00 * 0.18

# Calculate the totalCost
totalCost = subTotal + tipAmount
totalCost = 107.00 + 19.26

print('What is the tax?')
print('The tax is $',format(tax,',.2f'))
print('What is the sub total?')
print('The sub total is $',format(subTotal,',.2f'))                    
print('What is the tip amount?')
print('The tip amount is $',format(tipAmount,',.2f'))
print('What is the total cost of the bill?')
print('The total cost of the bill is $',format(totalCost,',.2f'))

