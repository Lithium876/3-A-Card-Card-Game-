from game import *
import time, os

players_in_game=[]
players_hand=[]
TotalNumOfPlayer = 0
house = Player("House")
deck = Deck()
banner='''
 _____         _          ____              _ 
|___ /        / \        / ___|__ _ _ __ __| |
  |_ \ _____ / _ \ _____| |   / _` | '__/ _` |
 ___) |_____/ ___ \_____| |__| (_| | | | (_| |
|____/     /_/   \_\     \____\__,_|_|  \__,_|
'''

def display():
	os.system("clear")
	print(banner)
	print("Deck has %d cards left"%(len(deck)))
	print("Current Card in play:")
	print("======================\n")
	house.showHand()
	print("\n======================")
	print("Your Hand: ")
	players_in_game[0].showHand()
	print("======================")

def startPlay():
	challengerPlay = False
	curr=house.getHand()

	for Player in players_in_game:
		display()
		if(Player.name == yourName):
			print("Your Turn")
		else:
			print(Player.name+"'s Turn")
		time.sleep(2)
		canplay = Player.checkHand(curr)

		if canplay and Player.name==yourName:
			display()
			op = input("Press ! to play or p to pass\n> ")
			if op == '!':
				pass
			elif op == 'p' or op == 'P':
				pass
		elif not canplay and Player.name==yourName:
			print("[-]No Play.....")
			time.sleep(2)
			while 1:
				draw = input("Press d to draw a card from the deck\n> ")
				if draw == 'd' or draw == 'D':
					break
				else:
					print("Invalid input.. Try Again")
					continue
			print("Drawing...")
			house.drawCard(deck)
			curr=house.getHand()
			time.sleep(2)
			display()

		elif canplay and Player.name!=yourName:
			print("%s can play enuh"%(Player.name))
			challengerPlay = True
			break
		else:
			time.sleep(2)
			print("[-]No Play.....")
			time.sleep(2)
			print("Drawing...")
			house.drawCard(deck)
			curr=house.getHand()
			time.sleep(2)
			display()

	if len(deck)==0:
		print("[-]Deck Empty")
	elif challengerPlay:
		pass
	else:
		time.sleep(3)
		os.system("clear")
		startPlay()
	
def startGame():
	global TotalNumOfPlayer 
	global yourName
	TotalNumOfPlayer = 0
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
		TotalNumOfPlayer = TotalNumOfPlayer + num_of_players + 1
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
	house.drawCard(deck)
	startPlay()

startGame()