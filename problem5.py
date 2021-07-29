"""Write a program that asks the user for a number n and gives them the possibility to 
choose between computing the sum and computing the product of 1,…,n.
"""

def ask_num():
    ask_number = int(input("Please enter a number \n"))
    return ask_number

def operation_choice(ask_number):
    print(f"please enter the operation you wish from 1 to {ask_number}\n1 - Addition\n2 - Multiplication")
    choice = int(input())
    return choice

def multiply(number):
    result = 1
    for i in range(1,number+1):
        result = result *i

    print(f"The product of numbers from 1 to {number} is {result}")

def add(number):
    result = 0
    for i in range(1, number+1):
        result = result + i
    print(f"The sum of numbers from 1 to {number} is {result}")


a = ask_num()
choice = operation_choice(a)
if choice == 1:
    add(a)
else:
    multiply(a)
  
