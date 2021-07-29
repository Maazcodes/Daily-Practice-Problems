# Modify the previous program such that only multiples of three or five are considered in the sum, e.g. 3, 5, 6, 9, 10, 12, 15 for n=17

def sumOfnumbersHere(number):
    """
    Modify the previous program such that only multiples of three or five are 
    considered in the sum, e.g. 3, 5, 6, 9, 10, 12, 15 for n=17
    """
    result = 0
    for i in range(1,number + 1):
        if i % 3== 0 or i % 5 == 0:
            result = result + i
    return result

ask_number = int(input("Enter the number\n"))

print(f"The sum of numbers from 1 to {ask_number} considering only multiples of 3 and 5 is {sumOfnumbersHere(ask_number)}")