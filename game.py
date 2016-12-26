import random

class Card:
	def __init__(self, suit, value ):
		self.suit = suit
		self.value = value

	def showCard(self):
		print("%s of %s"%(self.value,self.suit))

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

class Player:
	def __init__(self, name):
		self.name = name
		self.hand = []

	def drawCard(self, deck):
		self.hand.append(deck.drawCard())
		return self

	def showHand(self):
		for card in self.hand:
			card.showCard()