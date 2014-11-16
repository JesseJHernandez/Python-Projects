import random

def rock_paper_scissor(user_input):
	options = ["rock", "paper", "scissors"]

	if user_input.lower() in options:
		print "You picked %s " % (user_input)

	#Computer outputs their choice
	computer_choice = random.choice(options)
	print "Computer picked %s " % (computer_choice)

	#check to see if user choice equal computer choice - draw
	if user_input.lower() == computer_choice:
		print "It is a draw!"

	#RS,RP,PR,PS,SR,SP
	elif user_input.lower() == "rock":
	    if computer_choice == "scissors":
	        print "You win"
	    if computer_choice == "paper":
	        print "You lose"

	elif user_input.lower() == "paper":
		if computer_choice == "rock":
			print "You win"
		if computer_choice == "scissors":
			print "You lose"

	elif user_input.lower() == "scissors":
		if computer_choice == "rock":
			print "You lose"
		if computer_choice == "paper":
			print "You win"
	else:
		print "Your answer is invalid. Try again... "

def main():

	#Ask user if they want to play again
	while True:
		
		user_input = raw_input("Rock, Paper or Scissors? ")

		rock_paper_scissor(user_input) 


	 	while True:
	 		options2 = raw_input("Do you want to play again? ")
	 	
	 		if options2.lower() not in  ["yes", "no", "y", "n"]:
	 			print "Invalid response. Please try again. "
	 		else:
	 			break

		if options2.lower() in ["no","n"]:
	 		break


if __name__ == "__main__":

	main()



