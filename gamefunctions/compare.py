import time
from random import randint


def comparing (player, computer):
	global pwin
	global cwin
	global plives
	global clives

	if ( player == computer ):
		print ("  You and the computer chose the same! \n")
		print ( "\033[35m            ** Tie! **\033[30;0;0m" )

	elif ( player == "rock" ):
		if (computer == "paper"):
			print ("           Paper covers rock! \n")
			print (cwin)
			plives = plives - 1

		elif (computer == "scissors"):
			print ("          Rock smashes scissors! \n")
			print (pwin)
			clives = clives - 1

	elif ( player == "paper"):
		if (computer == "rock"):
			print ("           Paper covers rock! \n")
			print (pwin)
			clives = clives - 1

		elif (computer == "scissors"):
			print ("           Scissors cut paper! \n")
			print (cwin)
			plives = plives - 1


	elif ( player == "scissors" ):
		if ( computer == "paper"):
			print ("           Scissors cut paper! \n")
			print (pwin)
			clives = clives - 1

		elif (computer == "rock"):
			print ("          Rock smashes scissors! \n")
			print (cwin)
			plives = plives - 1

	else:
		print ("     Sorry, that's not a valid answer! ")
		#if an answer is not rock paper or scissors.
		