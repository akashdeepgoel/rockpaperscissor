#First Python Game
#Rock Paper Scissor - Implements Random number using Python standard random number generator
from random import *
import os
def choose():
	chosen = randint(1,3)
	return chosen

def findwinner(user_choice,pc_choice):
	win = "You Won!!\n"
	lose = "You Lose..I guess You are Unlucky\n"
	tie = "It is a tie!!\n"
	out = "PC Chose %s\n"
	choice = ""
	if pc_choice==1:
		choice+="Rock"
	elif pc_choice==2:
		choice+="Paper"
	else:	
		choice+="Scissor"
	if user_choice==pc_choice:
		print out%(choice)
		print tie
	elif user_choice>pc_choice:
		diff = user_choice - pc_choice
		if diff==1:
			print out%(choice)
			print win
		else:
			print out%(choice)
			print lose
	else:
		diff = pc_choice - user_choice
		if diff==1:
			print out%(choice)
			print lose
		else:
			print out%(choice)
			print win

def begin():
	print "Ok Let's Play!"
	choice = input("Enter Your Choice:\n Enter 1 if your choice is Rock\n Enter 2 if Your Choice is Paper \n Enter 3 if your choice is Scissor\n")
	return choice

def play():
	clear = lambda: os.system('clear')
	clear()
	user_choice = begin()
	pc_choice = choose()
	findwinner(user_choice,pc_choice)
	cont = input("Would You Like To Continue? (1 for Yes and 0 for No)")
	if cont==1:

		play()
	else:
		print "Hope you enjoyed!!"
		exit(0)
clear = lambda: os.system('clear')
clear()
print "Welcome To Rock,Paper Scissor!!!"
play()
