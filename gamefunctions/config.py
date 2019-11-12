from random import randint

choices = ["rock", "paper", "scissors"]
computer = choices[randint (0, 2)]
pwin = ("\033[32m            ** Player wins! ** \033[30;0;0m")
cwin = ("\033[31m            ** Comp wins! ** \033[30;0;0m")
tlives = 5
#tlives controls the number of player and computer lives!

plives = tlives
clives = tlives
player = False

#stating all your varibales
#can call anywhere as a config.variable to be global
