# Write a program that prints all prime numbers.

def check_prime_number(number):
    for i in range(2, number):
        if number % i == 0:
            return 'it is not a prime number'
    return '{} is a prime number'.format(number)

# print(check_prime_number(79))

def primeNumbers(number):
    for i in range(2,number):
        for j in range(2,i):
            # traverse or iterate over the numbers except 1 and the number
            if i%j ==0:
                break
        else:
            print(i)
               

primeNumbers(10)

