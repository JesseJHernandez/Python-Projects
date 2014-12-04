import random

roster = { "pikachu" : 10, 
			"charizard" : 25, 
			"mewtwo": 50, 
			"squirtle" : 15,
			"magikarp" : 0}



# welcome statement

# would you like to draw a pokemon

#randomly pick from the roster for the player:
#comupter picks from the roster
# winner gets decided

def pokemon_game():

	computer_choice = random.choice(roster.keys()) # Computer randomly selects pokemon
	comp_score = roster[computer_choice] 

	player_choice = random.choice(roster.keys()) # Computer randomly selects pokemon
	player_score = roster[player_choice]
	print "Computer has chosen %s " % (computer_choice)
	print "Player has chosen %s " % (player_choice)

	if comp_score > player_score:
		print "You lose. "

	if player_score > comp_score:
		print "You WIN! "

	if comp_score == player_score:
		print "You Tied. "


pokemon_game()



# would you 