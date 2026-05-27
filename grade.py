#Grecia C.
#Grades
#Write a function that asks the user to input a score as an integer and prints the appropiate letter grade

#Functions

score = int (input("Please enter your score: "))
if score >= 90:
    print ("Your grade is an: A")
elif score >= 80:
    print ("Your grade is a: B")
elif score >= 70:
    print ("Your grade is a: C")
elif score >= 60:
    print("You grade is a: D")
elif score <=50:
    print("Your grade is an: F")
#Main

