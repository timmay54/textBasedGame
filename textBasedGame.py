"""
Text based game written in python

began writting on 3/31/2018 @ 12:14 AM 

This game focuses on choosing wich tools are the handiest in the wrong run.

CONTROLS:







TO DO -

Needs to be connected to the dictionary for the players' items.

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
				break
			elif(response=="help"):
				print("You can: \nDrink water\nWalk outside\nLook in fridge\nCall someone on your phone.")
			else:
				print("You need help? Probaby should ask for some...")
		except Exception as e:
			print("Fatal error has occurred!\a")
		else:
			print ("You should ask for 'help'.")



dict_places = {
	
	1  : "kitchen"        ,
	2  : "bathroom"       ,
	3  : "living room"    ,
	4  : "stairs2"         ,
	5  : "stairs3"          , 
	6  : "attic"             , 
	7  : "tiny pink room"     ,
	8  : "angry man's room"    ,
	9  : "business man's room" , 
	10 : "the pig man's room"  , 
	11 : "the best man's room" ,
	12 : "front door"   
}

dict_kitchen = {
	
	"fridge"     : "You see some old ham, beer in the drawers, and jello shots." ,
	"cupboards"  : "Ramen, egg noodles, and jarred stuff from the business man." ,
	"Closet"     : "a red cooler, backpack, broom, and extra lightbulbs." 



}

dict_player_items = {
	

}

dict_startmenu = {
	1 : game_main()          ,
	2 : print ("How to play")        ,
	3 : "Puss the fuck out"   
}


"""This is the start menu of the game. This block runs first."""

print ("Welcome to _________!")
ans = input("1.Start\n2.How to play\n3.Puss the fuck out\n\n")
try:
	dict_startmenu[ans]
except Exception as e:
	print("fatal error in start block!")
else:
	print("else block in start block has been reached.")