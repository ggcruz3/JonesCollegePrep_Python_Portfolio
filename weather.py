#Grecia C.
#Weather
#Create a program that advises you on what clothing to wear and accessories to bring based on temperature given

#Function
weather = int(input("What is the temperature today?: "))
if weather >= 80:
    print ("Wear shorts and bring a pair of sunglasses")
elif weather >=60:
    print ("Wear jeans and put a sweater on ")
elif weather >= 40:
    print ("Wear a jacket and some gloves ")
elif weather <= 20:
    print("Put on a thick jacket so you stay warm and a longsleeve with some pants on ")
