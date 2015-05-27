#First Python Game
#Rock Paper Scissor - Implements Random number using Python standard random number generator
from random import *
def choose():
	chosen = randint(0,2)
	if chosen == 0:
		return "Rock"
	elif chosen == 1:
		return "Paper"
	else:
		return "Scissor"


def begin():
	print "Ok Let's Play!"
	choice = input("Enter Your Choice:\n Enter 1 if your choice is Rock\n Enter 2 if Your Choice is Paper \n Enter 3 if your choice is Scissor\n")
	return choice

def play():
	user_choice = begin()
	pc_choice = choose()
	if pc_choice=="Rock":
		if user_choice==2:
			print "PC Chose Rock\n"
			print "You Won!!\n"
		elif user_choice==1:
			print "PC Chose Rock\n"
			print "It is a tie!!\n"
		else:
			print "PC Chose Rock\n"
			print "You Lose..I guess You are Unlucky\n"

		cont = input("Would You Like To Continue? (1 for Yes and 0 for No)")
		if cont==1:
			play()
		else:
			print "Hope you enjoyed!!"
			exit(0)
	if pc_choice=="Scissor":
		if user_choice==2:
			print "PC Chose Scissor\n"
			print "You Lose..I guess You are Unlucky\n"
		elif user_choice==1:
			print "PC Chose Scissor\n"
			print "You Won!!\n"
		else:
			print "PC Chose Scissor\n"
			print "It is a tie!!\n"

		cont = input("Would You Like To Continue? (1 for Yes and 0 for No)")
		if cont==1:
			play()
		else:
			print "Hope you enjoyed!!"
			exit(0)
	if pc_choice=="Paper":
		if user_choice==2:
			print "PC Chose Paper\n"
			print "It is a tie!!\n"
		elif user_choice==1:
			print "PC Chose Paper\n"
			print "You Lose..I guess You are Unlucky\n"
		else:
			print "PC Chose Paper\n"
			print "You Won!!\n"

		cont = input("Would You Like To Continue? (1 for Yes and 0 for No)")
		if cont==1:
			play()
		else:
			print "Hope you enjoyed!!"
			exit(0)


print "Welcome To Rock,Paper Scissor!!!"
play()
