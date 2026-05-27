#Init
import time
import random
def main():
    print("Welcome to Hogwarts")
    name = input("What is your name: ")
    time.sleep(1)
    print("..")
    time.sleep(1)
    print("....")
    time.sleep(1)
    print("......")
    print(house(name))
    while True:
        Play = input("Would you like to be reassaigned to a new house?")
        if Play == "yes":
            main()
        else:
            print("That's fine!")
            break


def house(name):
    if name == "Harry" or name == "Hermione" or name == "Ron":
        return "Gryffindor"
    if name == "Newt" or name == "Nymphadora" or name == "Pomona":
        return "Hufflepuff"
    if name == "Luna" or name == "Cho" or name == "Filius ":
        return "Ravenclaw"
    if name == "Voldemort" or name == "Draco" or name == "Severus ":
        return "Slytherin"

    else:
        num = random.randint(1,4)
        if num == 1:
            return "Gryffindor"
        if num == 2:
            return "Hufflepuff"
        if num ==3:
            return "Ravenclaw"
        if num ==4:
            return "Slytherin"

#Main
main()
