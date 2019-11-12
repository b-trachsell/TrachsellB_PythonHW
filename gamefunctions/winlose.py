from random import randint
from gamefunctions import config
import time

#defining a variable
def winolose(status):


	print ("\n\n \033[34m ----------------------------------------------------\033[30;0;0m" )
	print ("\n\n     You ", status )
	print ("      Would you like to play again? \n")
	choice = input ("                Y / N \n")

	if (choice == "N" or choice == "n"):
		print ("\n\n\n              Thank you for playing!\n\n\n")
		exit ()

	elif (choice == "Y" or choice == "y"):
                print ("\n\n Preparing to start again... ")
                config.plives = 5
                config.clives = 5
                
	else:
		#use recursion to call winolose until the right input :)
		#Call the function within the function to make it do the thing again.
		print ("\n       Sorry, that's not an option!")
		time.sleep (0.8)
		winolose(status)
