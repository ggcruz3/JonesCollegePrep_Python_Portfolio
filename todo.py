#Grecia
#Create the To-do List App that allows the user to keep track of items that must get done during the day

#Func
print("Welcome to the Movies to watch app!")
movies = [
        "Inside Out","Interstellar","Star Wars","Spider-Man","Toy Story","Joker","Grown Ups","Jaws"
        ]
finished_movies=[]
def list():
    while True:
            options=input("""
    Decide what you would like to do:
    1. Add a specific movie to the watch list
    2. Mark a movie as watched
    3. Remove a movie from the watch list
    4. Exit the program
    Enter a number: """)
            if options == "1":
                print(movies)
                name = input("What movie would you like to add: ").strip()
                if name == "":
                    print("Sorry, but that is not a valid response. ")
                else:
                    movies.append(name)
                    print(f"Updated Watchlist:{movies}")
                    continue
            elif options == "2":
                print(movies)
                done=input("What movies have you finished watching: ")
                movies.remove(done)
                finished_movies.append(done)
                print(f"Watchlist: {movies}")
                print(f"Finished Movies: {finished_movies}")
                continue
            if options == "3":
                print(movies)
                gone=input("What movie would you like to remove? ")
                movies.remove(gone)
                print(f"Watchlist: {movies}")
                print(f"Finished Movies: {finished_movies}")
                continue

            elif options == "4":
                print("Goodbye")
                break
#Main
list()

