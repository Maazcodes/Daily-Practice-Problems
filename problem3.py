# Write a program that asks the user for a number n and prints the sum of the numbers 1 to n

def sumOfNumbers(number):
    """
    Write a program that asks the user for a number n and prints the sum of the numbers 1 to n
    """
    result = 0
    for i in range(1, number+1):
        result = result + i
    return result


ask_the_number = int(input('Please enter the number \n'))

print(f"the sum of numbers from 1 to {ask_the_number} = {sumOfNumbers(ask_the_number)} ")