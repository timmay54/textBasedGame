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

"""

import platform #this is for determining the computer running the file
import time

"""
These are objects that will be called throughout the game

"""

dict_places = {

	1  : "kitchen"             ,
	2  : "bathroom"            ,
	3  : "living room"         ,
	4  : "stairs2"             ,
	5  : "stairs3"             ,
	6  : "attic"               ,
	7  : "tiny pink room"      ,
	8  : "angry man's room"    ,
	9  : "business man's room" ,
	10 : "the pig man's room"  ,
	11 : "the best man's room" ,
	12 : "front door"          ,
}

dict_kitchen = {

	"fridge"     : "You see some old ham, beer in the drawers, and jello shots." ,
	"cupboards"  : "Ramen, egg noodles, and jarred stuff from the business man." ,
	"Closet"     : "a red cooler, backpack, broom, and extra lightbulbs."

}

dict_player_items = {


}

"""
dict_startmenu = {
	"1"   : game_main           ,
	"2"   : "How to play"        ,
	"3"   : "Quit"   ,
}
"""

"""   GAME BLOCK    """

def game_main():
	startGame = True
	lives = 3
	itemMAX = len(dict_player_items)
	response = input("You are standing in a kitchen, dazed and confused.")
	while (response != "quit"):
		try:
			if (response == "smoke weed"):
				print("holy fuck you just won the universe")

			elif(response=="help"):
				print("You can: \nDrink water\nWalk outside\nLook in fridge\nCall someone on your phone.")
			else:
				print("You need help? Probaby should ask for some...")
		except Exception as e:
			print("Fatal error has occurred!\a")
		else:
			print ("You should ask for 'help'.")

"""This is the start menu of the game. This block runs first."""

def start_menu():
	print ( platform.platform() )
	print ( platform.system()   )
	print ( platform.release()  )
	print ( platform.version()  )
	print ("This is determining your computer type and brand")

	print ("Welcome to _________!")
	ans = int(input("1. Start\n2. How to play\n3. Quit\n\n") ) ###had to change this for online purposes LOL

	print ("\nYou have entered " + ans)

	try:
		if (ans == 1 or ans == "1"):
			game_main()
		elif (ans == 2 or ans == "2"):
			print (dict_startmenu[2])
		elif (ans == 3 or ans == "3"):
			print (dict_startmenu[3])
		else:
			print("*****else block")

	except Exception as e:
		print("fatal error in start block")


start_menu()
