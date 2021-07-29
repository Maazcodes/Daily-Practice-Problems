# Write a program that prints a multiplication table for numbers up to 12.

def multiplicationTable(number):
    for i in range(1,13):
        result = number*i
        print(f"{number} * {i} = {result}")

def number_choice():
    choice = int(input("Enter a number\n"))
    return choice

multiplicationTable(number_choice())