import random


class Deck:

	def __init__(self):
		self.deck = []
		self.suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
		self.ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
		self.values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11}

		for suit in self.suits:
			for rank in self.ranks:
				self.deck.append((suit, rank))

	def shuffle_deck(self):
		random.shuffle(self.deck)

	def __str__(self):
		return str(self.deck)
				

class Player:

	def __init__(self, name, bank_bal):
		self.name = name
		self.bank_bal = bank_bal
		self.values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11}

	def __str__(self):
		pass

	def bet(self, bet):
		while self.bank_bal < bet:
			bet = int(input('Enter bet again: '))
		else:
			return bet
	
	def hand(self, hnd):
		self.sum_cards = 0
		for suit, rank in hnd:
			if self.values[rank] != 11:
				self.sum_cards = self.sum_cards + self.values[rank]
			else:
				if self.sum_cards > 10:
					self.sum_cards = self.sum_cards + 1
				elif self.sum_cards <= 10:
					self.sum_cards = self.sum_cards + 11
		return self.sum_cards

class Comp_Dealer:
	def __init__(self, bank_bal = 100, name = 'Computer'):
		self.name = name
		self.bank_bal = bank_bal
		self.values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11}

	def hand(self, hnd):
		self.sum_cards = 0
		for suit, rank in hnd:
			if self.values[rank] != 11:
				self.sum_cards = self.sum_cards + self.values[rank]
			else:
				if self.sum_cards > 10:
					self.sum_cards = self.sum_cards + 1
				elif self.sum_cards <= 10:
					self.sum_cards = self.sum_cards + 11
		return self.sum_cards

def chips_check(name,chips):
	print(f'{name} has {chips} chips')
	if chips <= 0:
		print(f'{name} is out of chips. Reload again')
		return True

def hit(deck):
	card = deck.pop()
	return card

def deal(deck):
	card1 = deck.pop()
	card2 = deck.pop()
	return card1, card2

def replay(choice, chips1, chips2):
	if chips1 <= 0 or chips2 <= 0:
		return True
	elif choice.lower() == 'yes':
		return True
	else:
		return False

def win(sum_of_hand):
	if sum_of_hand == 21:
		return 'Won'
	elif sum_of_hand > 21:
		return 'Bust'
	elif sum_of_hand < 21:
		return 'Not yet'


name = input('Enter your name: ')
chips = int(input('Enter the number of chips you have: '))
player = Player(name, chips)
comp = Comp_Dealer()
game = True

while game:
	hand = []
	game_deck = Deck()
	game_deck.shuffle_deck()
	player_bet = player.bet(int(input('Place your bet: ')))


		
	game_on = True
	while game_on:
		w = 0
		player_hand = []
		comp_dealer_hand = []
		for card in deal(game_deck.deck):
			player_hand.append(card)
		for card in deal(game_deck.deck):
			comp_dealer_hand.append(card)
		print(f"{player.name}'s hand: {player_hand}")
		print(f"computer's hand: {comp_dealer_hand[0]}")
		player_sum_of_cards = player.hand(player_hand)
		print(player_sum_of_cards)
		if win(player_sum_of_cards) == 'Won':
			print(f'{player.name} won')
			player.bank_bal = player.bank_bal + player_bet
			comp.bank_bal = comp.bank_bal - player_bet
			if chips_check(player.name, player.bank_bal) == True:
				break
			break
		comp_sum_of_cards = comp.hand(comp_dealer_hand)
		print(comp_sum_of_cards)
		if win(comp_sum_of_cards) == 'Won':
			print(f'{comp.name} won')
			player.bank_bal = player.bank_bal - player_bet
			comp.bank_bal = comp.bank_bal + player_bet
			if chips_check(comp.name, comp.bank_bal) == True:
				break
			break
		while input('Do you want to hit or stay. Enter H for hit and S for stay: ').lower() == 'h':
			card = hit(game_deck.deck)		
			player_hand.append(card)
			print(player_hand)
			player_sum_of_cards = player.hand(player_hand)
			print(player_sum_of_cards)
			if win(player_sum_of_cards) == 'Not yet':
				continue
			elif win(player_sum_of_cards) == 'Won':
				print(f'{player.name} won')
				w = 1
				player.bank_bal = player.bank_bal + player_bet
				comp.bank_bal = comp.bank_bal - player_bet
				break
			elif win(player_sum_of_cards) == 'Bust':
				print('Bust!! You Lost')
				print(f'{comp.name} won')
				w = 1
				player.bank_bal = player.bank_bal - player_bet
				comp.bank_bal = comp.bank_bal + player_bet
				break
		if w != 1:
			while comp_sum_of_cards < 21:
				card = hit(game_deck.deck)
				comp_dealer_hand.append(card)
				print(comp_dealer_hand)
				comp_sum_of_cards = comp.hand(comp_dealer_hand)
				if win(comp_sum_of_cards) == 'Bust':
					print(f'{player.name} won')
					player.bank_bal = player.bank_bal + player_bet
					comp.bank_bal = comp.bank_bal - player_bet
					break
				elif comp_sum_of_cards > player_sum_of_cards:
					print(f'{comp.name} won')
					player.bank_bal = player.bank_bal - player_bet
					comp.bank_bal = comp.bank_bal + player_bet
					break
				elif comp_sum_of_cards < player_sum_of_cards:
					continue

		break
	if chips_check(player.name, player.bank_bal):
		break
	if chips_check(comp.name, comp.bank_bal):
		break

	choice = input('Enter Yes to play again: ')

	if not replay(choice, player.bank_bal, comp.bank_bal):
		game = False 
























