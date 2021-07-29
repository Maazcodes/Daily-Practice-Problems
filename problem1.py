# Write a program that asks the user for their name and greets them with their name.

def your_name(name):
    return f'Good Morning {name}'

my_name = input('What is your name?\n')
print(your_name(my_name))