import random

random_number = random.randint(1,50)

print("Guess the secret number between 1 and 50 in 10 chances.\n")

guess_num_lst = []

i = 1
while i < 11:

    print(f"You have {11-i} chances left")
    guess_number = int(input())
    if guess_number in guess_num_lst:
        print("You have repeated the number")
        continue
    guess_num_lst.append(guess_number)
    print(f"Your guessed numbers are {guess_num_lst}")

# 100-2*(i-1)*10
# 100-2*10
# 100-2*20
# 100-2*30
# 100-2*40

    if i in range(1,6) and guess_number == random_number:
        print(f"Great, you have guessed the secret number! It is {random_number}\nCongratulations, You have scored {100-2*(i-1)*10} points")
        break

    if i > 4 and guess_number == random_number:
        print(f"Great, you have guessed the secret number! It is {random_number}")
        print("You have only scored 10 points. Shame on you!")
        break

    if i == 6:
        print(f"The number is between {random_number-9} and {random_number+7}")
    elif i == 7:
        print(f"The number is between {random_number-4} and {random_number+5}")
    elif i== 8:
        print(f"The number is between {random_number-2} and {random_number+3}")
    elif i == 9:
        print(f"The number is between {random_number-1} and {random_number+2}")
    else:
        pass

    i+=1
else:
    print(f"Try next time, the secret number is {random_number}")

