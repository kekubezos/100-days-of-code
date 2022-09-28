# Author: Mayfred Kekeli Norgbey
# Project: Tip Calculator

print('Welcome to the tip calculator!')

bill = float(input('What\'s the total bill? $'))
tip = int(input('What percentage tip will you like to give? 10,12 or 15\t'))
number_of_people = int(input('How many people will split the bill?\t'))

bill_with_tip = bill * (1 + tip/100)

actual_bill = bill_with_tip / number_of_people
actual_bill = round(actual_bill, 2)


print(f'Each person should pay: ${actual_bill}')

