from itertools import chain
import random, time

class Card:
	def __init__(self, suit, value ):
		self.suit = suit
		self.value = value

	def showCard(self):
		print("%s of %s"%(self.value,self.suit))

	def getCard(self):
		return("%s %s"%(self.value,self.suit))

class Deck:
	def __init__(self):
		self.cards = []
		self.buildDeck()

	def buildDeck(self):
		for suit in ["Hearts", "Clubs", "Diamonds", "Spades"]:
			for value in range(1, 14):
				if value == 1:
					self.cards.append(Card(suit,"Ace"))
				elif value == 11:
					self.cards.append(Card(suit,"Jack"))
				elif value == 12:
					self.cards.append(Card(suit,"Queen"))
				elif value == 13:
					self.cards.append(Card(suit,"King"))
				else:
					self.cards.append(Card(suit,value))

	def showDeck(self):
		for card in self.cards:
			card.showCard()

	def shuffleDeck(self):
	#Fisher-Yates shuffle 
		for i in range (len(self.cards) -1,0,-1):
			rand = random.randint(0,i)
			self.cards[i], self.cards[rand] = self.cards[rand], self.cards[i]

	def drawCard(self):
		return self.cards.pop()

	def __len__(self):
		return len(self.cards)

class Player:
	house =[]
	def __init__(self, name):
		self.name = name
		self.hand = []

	def __len__(self):
		return len(hand)
		
	def drawCard(self, deck):
		self.hand.append(deck.drawCard())
		return self

	def showHand(self):
		for card in self.hand:
			card.showCard()

	def playCard(self, playCard):
		Player.house.append(playCard)
		self.hand.pop()
		return self

	def getHand(self):
		arr_cards_in_hand=[]
		for card in self.hand:
			arr_cards_in_hand.append(card.getCard().split(' '))#create a list of lists here
		return list(chain.from_iterable(arr_cards_in_hand)) #returns flatten list

	def checkHand(self,current_card):
		print("[+]%s needs a %s to of any suit to play..."%(self.name, current_card[len(current_card)-2]))
		time.sleep(2)
		for card_in_hand in self.hand:
			card=card_in_hand.getCard().split(' ')
			if card[0] in current_card[len(current_card)-2]:
				return True
			else:
				pass