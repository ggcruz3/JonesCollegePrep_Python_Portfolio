import random

print("Welcome! Today you are going to guess a num.")

number =int(input("Please enter the number you think it is: "))

while True:
        chance = input("Enter password: ")
        password = "python"

        if chance == "python":
            print("Access granted!")
            break
        else:
            print("Incorrect password. Try again")
            continue
