"""
THIS WILL HOLD ALL OF THE ROOM FUNCTIONS

Why?

So python is weird, and it reads the file from top to bottom. All languages do this,
but I don't know how to get the stuff that hasn't been read yet to be called, nor
will the previous method work when trying to go back to a room you have already
been in. To do that, you'd need to call a function that might not have been "read"
yet, crashing the program. By defining all the functions here, and then importing
them all to the main program file, we basically make it easier to:
1. edit the code to change the game
2. make it simpler to understand and to read
3. to organize which functions need called first (now it doesnt matter the order!)

so yeah, we are now ready to get as creative as possible, and you guys can throw in
whatever you want to try out! I won't edit your stuff, you keep trying to figure it
out and ill be here for questions!

"""

def frontDoor():
    frontDoorMenu = {
    1 : "Go look at the bush.",
    2 : "Go to on the east side of the house.",
    3 : "Got to the West side of the house.",
    4 : "Go look in the Man hole cover by the steps.",
    5 : "Go back inside the house.",

    }
    print("Well, there's a bush carved like a dick outside. How nice.")
    print(frontDoorMenu)
    try:
        ansFD = input()

        if ansFD == 5:
            livingRoom()
        elif ansFD == 4:
            manHole()
        elif ansFD == 3:
            stairs1()
    except Exception as e:
        print("How about you type a number in.")


def manHole():
    manHoleMenu = {
    1 : "Go back to the front of the house.",
    #there will be ALOT of stuff going on down here.
    }
    print("The best man was here, he used to hide from the cops down in these tunnels.")
    print("The tunnels don't exactly run parallel with the roads, but I bet you'll figure it out.")
    playerScore = playerScore + 1000
    while(True):
        try:
            ansMH = input(manHoleMenu)
            if (ansMH == 1) or (ans == "front door"):
                frontDoor()
        except Exception as e:
            print("Idiot, type something relevant!")

def stairs1():
    stairs1Menu = {
    1 : "Fiddle with experiment tools!",
    2 : "open the crappy door",
    3 : "mess with furnace",
    4 : "look at stuff on shelf",
    5 : "go back upstairs",
    }
    print("Welcome to the secret Labratory. The man that lived in the tiny pink room conducted")
    print("weird ass experiments down here. The furnace looks jank and it smells awful down here.")
    try:
        ansS1 = input(stairs1Menu)

        if ansS1 == 5:
            livingRoom()

    except Exception as e:
        print("How have you not figured this out yet.")
