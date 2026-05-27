#Grecia C.
#Generate and print out the lyrics to the song "99 Bottles of Milk on the Wall."


#Func
def bottle():
    for x in range(100, -1, -1):
        if x>1:
            print(f"{x} bottles of milk on the wall, {x} bottles of millk.")
            print(f"Take one pass it around, {x-1} bottles of milk on the wall.")
        elif x ==1:
            print(f"{x} bottle of milk on the wall, {x} bottle of millk.")
            print("Take one pass it around, no more bottles of milk. ")
        else:
            print("No moere bottles of milk on the wall, Boo Hoo!")


#Main
bottle()
