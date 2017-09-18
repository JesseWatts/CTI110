# CTI-110 
# M2T1 - Sales Prediction 
# Jesse Watts
# 7 Sep 17
# Get the total projected sales.

# Get the projected total sales.
total_sales=float(input('Enter the projected sales:'))

# Calculate the profit as 23 percent of total sales.
profit=total_sales*0.23

# Display the profit.
print('The profit is $', format(profit, ',.2f'))
