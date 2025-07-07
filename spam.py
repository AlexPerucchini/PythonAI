spam = 0
print("Enter a 1 or 2 for a proper greeting...")
value = input()
print(f"Value entered = {value}...")
if value == "1":
    print("Howdy, stranger!!")
elif value == "2":
    print("Greetings, friend!!")
else:
    print("I am not sure you exist!!")
