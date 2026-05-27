#Grecia
#Asking the User what they would like to do
def adventure():
    print("Welcome to today's adventure! ")

    #Asks user where they want to go
    location = input ("Do you want to go to the beach or park? ")
    #User picked beach
    if location == "beach":
        activity = input("Would you like to go swim or stay in the sand? ")
        if activity == "sand":
            print ("Have fun building sand castles!")
        else:
            print("Congratulations you found a gold starfish!")
    #User picked the park
    else:
        activity = input("Would you like to go the swing or play in the slide? ")
        if activity == "swing":
            print("While you were there you made a new friend!")
        else:
            print("OH noooo! You broke your arm :( ")

#Main
adventure()


