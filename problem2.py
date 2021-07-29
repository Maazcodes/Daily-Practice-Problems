# Modify the previous program such that only the users Alice and Bob are greeted with their names.

def your_name(name):
    """
    Modify the previous program such that only the users Alice and Bob are greeted with their names.
    """
    return f'Good morning {name}'

public_name = input('What is your name?\n')

if public_name.capitalize() == 'Alice':
    print(your_name(public_name))
elif public_name.capitalize() == 'Bob':
    print(your_name(public_name))
else:
    print('Thanks')
