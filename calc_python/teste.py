# Now, let's import our calculator module into this script:
import calc
# Requesting values from the user:
value1 = input('Type a number: ')
value2 = input('Type another number: ')
# Storing the sum:
sum = calc.adding(value1, value2)
# Displaying it:
print('The sum is: {}'.format(sum))
# Doing the same with the other functions of the module:
division = calc.dividing(value1, value2)
print('A divisão é: {}'.format(division))
# Doing the same by placing the function call inside the .format:
multiplication = print('A multiplicação é {}'.format(calc.multiplying(value1, value2)))


# Another way
subtracao = print('A subtração é {}'.format(calc.subtracting(value1, value2)))

# We can select specific functions from the module using the "from" command:
# Importing specific functions from the calc.py module
from calc import adding, subtracting, multiplying, dividing
# Requesting values from the user:
value1 = input("Type a number: ")
value2 = input("Type another number: ")
# Storing the sum:
sum = adding(value1, value2)
# Displaying the sum:
print("The sum is {}".format(sum))
# And the subtraction:
subtraction = print('The subtraction is {}'.format(subtracting(value1, value2)))

# Multiplication:
multiplication = print('The multiplication is {}.'.format(multiplying(value1,value2)))

# Finally, division:
division = print('The division is {}'.format(dividing(value1,value2)))





