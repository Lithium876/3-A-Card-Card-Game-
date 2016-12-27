from game import *
import time, os

players_in_game=[]
deck = Deck()
banner='''
 _____         _          ____              _ 
|___ /        / \        / ___|__ _ _ __ __| |
  |_ \ _____ / _ \ _____| |   / _` | '__/ _` |
 ___) |_____/ ___ \_____| |__| (_| | | | (_| |
|____/     /_/   \_\     \____\__,_|_|  \__,_|

'''

def startGame():
	print(banner)
	yourName = input("Enter Your Name: ")
	you = Player(yourName)
	players_in_game.append(you)
	print("\nMaximum bots allowed: 8")
	print("Minimum bots allowed: 1\n")
	num_of_players = int(input("How many challengers in game (bots): "))
	if num_of_players > 8:
		print("The maximum ride number of players is 9")
		time.sleep(2)
		os.system("clear")
		startGame()
	elif num_of_players < 1:
		print("The minimum number of players is 1")
		time.sleep(2)
		os.system("clear")
		startGame()
	else:
		createNames=input("Would you like to give each challenger a name? (y or n)")
		if createNames == 'y' or createNames == 'Y':
			for i in range(1,num_of_players+1):
				player_name = input("Enter player's %s name: "%(i+1))
				players_in_game.append(player_name) 
				players_in_game[i]=Player(players_in_game[i])
		elif createNames == 'n' or createNames == 'N':
			for i in range(1,num_of_players+1):
				players_in_game.append("Player %s"%(i+1)) 
				players_in_game[i]=Player(players_in_game[i])
		getPlayersHand()

def getPlayersHand():
	time.sleep(1)
	print("Shuffling Deck...")
	deck.shuffleDeck()
	time.sleep(2)
	os.system("clear")
	print(banner)
	print("Handing out cards...")
	for i in range(1,4):
		for player in players_in_game:
			print(player.name+" Got %d card\n"%(i))
			player.drawCard(deck)
			time.sleep(1)
			os.system("clear")
			print(banner)
			print("Handing out cards...")
		player.getHand()
	os.system("clear")
	print(banner)
	print("Your Hand: ")
	players_in_game[0].showHand()
		

startGame()
