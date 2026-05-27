#Grecia C.
#Program defines a dunction 3 funvtions that simulate transactions in an atm

#Fuc
amount = 0
def atm():
    global amount
    print(f"Balance = {amount}")
    number1 =int(input("How much are you depositing: "))
    number2 = int(input("How much are you withdrawing: "))
    new = amount + number1 +- number2
    print(f"Balnce = {new}")

#Main
atm()

