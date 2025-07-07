# Write your code here :-)
name = ''
num_of_guests = ''
while not name or not name.isalpha():
    print('Enter your name:')
    name = input('>')
    if name.isalpha():
        print(f"Well hello, {name.upper()}")
        print('How many guests will you have?')
        while not num_of_guests or not num_of_guests.isdigit():
            num_of_guests = input('>>')
            if num_of_guests.isdigit():
                print('Be sure to have enough room for all your guests.')
                print('NOW EXITING THE MATRIX')
            else:
                print("ERROR: NOT A NUMBER")
    else:
        print("ERROR: INVALID NAME TYPE")
