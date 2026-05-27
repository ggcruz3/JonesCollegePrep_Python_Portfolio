#Grecia
#Asking user questions in order to give them what character they match with
def nickname():
    print("Hello, are you interested in knowing what character you are? Answer these questions and you will find out! ")
    Season = input ("Do you like fall or winter? ")
    #User picked Winter
    if Season == "winter":
        friends = input("Would you like stay home or go out friends? ")
        if "home" in friends:
            singing = input("Do you like singing (yes, no)? ")
            if singing =="yes":
                print("Congratulations you and Elsa are alike!")
            else:                                       #Giving them the final conclusion
                print("Congratulations you are like the Grinch!")
        else:
            independent= input("Would you describe yourself as independent (yes,no)? ")
            if independent=="yes":
                print("Congratulations you are like Mickey Mouse!")
            else:
                print("Congratulations you and Clifford the Big Red Dog are alike!")
#User picked fall
    elif Season=="fall":
            activity = input("Do you pefer apple picking or pumpkin patches? ")
            if "apple picking" in activity:
                snack = input("Do you like carrots or milk? ")
                if "carrots" in snack:
                    print("You are like Bugs Bunny congratulations! ")
                else:
                    print("Congratulation you are like Snoopy!")
            elif "pumpkin" in activity:
                choice = input("Do you prefer baking or eating pasta? ")
                if "baking" in choice:
                    print("Congratulations you are just like Hello Kitty!")
                else:
                    print("Congratulations you are just like Garfield!")
#Main
nickname()

