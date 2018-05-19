"""
Text based game written in python

began writting on 3/31/2018 @ 12:14 AM

This game focuses on choosing wich tools/items are the handiest in the long run.

CONTROLS:
planning to have each menu be a numbered item. Some items will be harder to find, and the
player will have to just know the number since it wont be listed (like a cheat code).


TO DO -

itemMAX needs to be connected to the dictionary for the players' items.

Add a timer, and it will save the lowest time of who completes the game the fastest
these things should probably be moved to the readme...



if windows, you need to clear window with os.system('cls')
if terminal, clear with os.system('clear')
find a pattern that works for clearing teriminal by setting a variable based on platform.os output

"""
import platform, time, os
import extraFunctions as aa

playerScore = 0
continueGame = False
lives = 3


"""
These are objects that will be called throughout the game

"""

kitchenMenu = {
	1  : "Kitchen"             ,
	#2  : "bathroom"            ,
	3  : "Living Room"         ,
	14 : "stairs1"             ,
	#4  : "stairs2"             ,
	#5  : "stairs3"             ,
	#6  : "attic"               ,
	#7  : "tiny pink room"      ,
	#8  : "angry man's room"    ,
	#9  : "business man's room" ,
	#10 : "the pig man's room"  ,
	11 : "the best man's room" ,
	#12 : "front door"          ,
	"fridge"     : "You see some old ham, beer in the drawers, and jello shots." ,
	"cupboards"  : "Ramen, egg noodles, and jarred stuff from the business man." ,
	"Closet"     : "a red cooler, backpack, broom, and extra lightbulbs."
}

livingRoomMenu = {
	1 : "Front Door"         ,
	2 : "stairs2"            ,
	3 : "the best man's room",
	4 : "Kitchen"            ,
}
def livingRoom():
	try:
		print("You are standing in the living room. There is a bag hanging from the ceiling fan.")
		print(livingRoomMenu)
		ansLR = input()

		if (ansLR == 1):
			game_main()

	except Exception as e:
		print("Input did not match any options, idiot.")

dict_player_items = {
	#phone maybe???
	2 : "45$"
}

def endGameStats():
	#subtract end time from start time.
	#create file (if file doesn't already exist)
	#scan to see if the user's current time is better than any of the top ten
	#if yes, then replace user's time with that number, and shift all worse times down the list

	#could add a variable below that determines what gets printed, between you suck, you have completed the game, and something awesome.
	if playerScore>10:
		print("Well, you atleast did okay.")
		print(playerScore)

	elif playerScore<10:
		print("you lost, you suck!")

def game_main():

	itemMAX = len(dict_player_items)
	response = "boobs"
	while ((response != "quit") ): # & (continueGame == True)
		try:
			print("You are standing in a kitchen, dazed and confused.\n")
			print(kitchenMenu)
			response = input()

			if (response == "smoke weed"):
				print("Holy fuck you just won the universe.\n")
				#play audio OOOHHHH FUCCKKK mlg
				"""for num in range(0,10000):
					playerScore = playerScore + 100"""
				print("Look at your score!!!", playerScore)
				continueGame = False
				return

			  #use a REGEX here to see if response has the
			  #words "living room" in it, which would eliminate a bunch of "or's"
			elif(response == "living room") or (response == "go to living room") or (response == 3):
				livingRoom()

			elif(response == "stairs1") or (response == "go to stairs1") or (response == "14") or (response == 14):
				aa.stairs1()

			else:
				print("You need help? Probaby should ask for some...")
				#pause here

		except Exception as e:
			print("Fatal error has occurred!\a")
		else:
			print ("You should ask for 'help'.")

def start_menu():                  #This probably doesnt need to be inside a funtion block lol
	print ( platform.platform() )
	print ( platform.system()   )
	print ( platform.release()  )
	print ( platform.version()  )
	print ("This is determining your computer type and brand.")

	print ("Welcome to _________!")
	ans = int(input("1. Start\n2. How to play\n3. Quit\n\n") )

	print ("\nYou have entered", ans)

	try:
		if (ans == 1 or ans == "1"):
			game_main()
		elif (ans == 2 or ans == "2"):
			print (dict_startmenu[2])
		elif (ans == 3 or ans == "3"):
			print (dict_startmenu[3])
			return
		else:
			print("*else block*")

	except Exception as e:
		print("fatal error in start block")


start_menu()

if continueGame == True:
	game_main()
elif continueGame == False:
	endGameStats()
