# Write your code here :-)
import random
import string

response = ''

#generates a randomized 12  characters password
def pass_randomizer(response):
    length = int(response)
    password = ''
    special_char = '%*!#'
    seed = string.ascii_letters + string.digits + special_char
    for i in range(length):
        password += random.choice(seed)
    return password

print('>> New password creation. Type quit to exit.')
#calling the function
while not response or not response.isdigit() or not response == 'quit':
    response = input('>> How many characters should your new password be? ')
    if response.isdigit():
        rand_password = pass_randomizer(response)
        print("Password: " + rand_password)
        print(f"Password length:{len(rand_password)}")
    elif response.lower() == 'quit':
        print("Exiting the program!")
        #sys.exit(0)
        quit()
    else:
        print("Error not a digit!")
