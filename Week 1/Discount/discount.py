# The store wants to increase sales on Tuesday and Wednesday
# If a sale of $50 or more takes place on Tuesday or Wednesday, apply a 10% discount
import datetime

# Initial sale cost
sale = float(input("How much did you spend?\n> "))

# Grab the date, then determine if it is Tuesday or Wednesday
date = datetime.datetime.now().weekday()

# Apply discount (1 = Tuesday, 2 = Wednesday)
if (date == 1 or date == 2) and sale >= 50:
    sale *= .9 


print(f"Your total is: ${sale:.2f}")