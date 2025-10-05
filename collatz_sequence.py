import sys

def collatz(number):
    if number % 2 > 0:  #determines if number is even or odd by testing for a remainder
        number_odd_result = 3 * number + 1
        print(str(number_odd_result) + ' <--odd')
        return number_odd_result
    else:
        number_even_result = number // 2
        print(str(number_even_result) + ' <--even')
        return number_even_result

while True:     #while loop continues until user enters a number.
    try:
        i = int(input('Enter any integer: '))
        break
    except ValueError:
        print("You must enter an integer.")
        continue

while i != 1:
    i = collatz(i)
    print(' ' * (i // 2) + '.')     #adds a period spaced out by i divided by 2

