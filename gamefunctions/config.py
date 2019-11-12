from random import randint

choices = ["rock", "paper", "scissors"]
computer = choices[randint (0, 2)]
pwin = ("\033[32m            ** Player wins! ** \033[30;0;0m")
cwin = ("\033[31m            ** Comp wins! ** \033[30;0;0m")
plives = 5
clives = 5
player = False
