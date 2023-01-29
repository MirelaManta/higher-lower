from game_data import data
from art import logo, vs
import random
from replit import clear

def get_random_account(data):
	''' This gets a random account from the list with all of accounts'''
	rand_account = random.choice(data)
	return rand_account

def format_data(rand_account):
	'''It takes the account randomly chosen and format the containing data in a desired way, through the help of keys'''
	name = rand_account["name"]
	description = rand_account["description"]
	country = rand_account["country"]
	return f"{name}, a {description}, from {country}."

def compare_answer(answer, followers_A, followers_B):
	'''Compares the user's response with the correct one and returns True if they got it right, else False'''
	if followers_A > followers_B:
		return answer == "a"
	else:
		return answer == "b"

def game():
	print(logo)
	score = 0
	game_continues = True
	account_A = get_random_account(data)
	account_B = get_random_account(data)
	
	while game_continues:
		account_A = account_B
		account_B = get_random_account(data)	
		# making sure the accounts are different and if they are not, changing the values by generating another account
		while account_A == account_B:
			account_B = get_random_account(data)
		
		print(f"Compare : {format_data(account_A)}")
		print(vs)
		print(f"Against B: {format_data(account_B)}")
		answer = input("Who has more followers? Type 'A' or 'B'..").lower()
		
		followers_A = account_A["follower_count"]
		followers_B = account_B["follower_count"]
		right_answer = compare_answer(answer, followers_A, followers_B)
		
		# clear the screen between rounds
		clear()
		print(logo)
			
		if right_answer:
			score += 1
			print(f"You're right! Current score: {score}")
		else:
			game_continues = False
			print(f"{followers_A}, {followers_B}")
			print(f"Wrong answer! Final score: {score}")

game()
		
	
	
		
		
		
	
	
	





	

