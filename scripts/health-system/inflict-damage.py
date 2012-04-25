##################################################
### Awesome Damage Script! ### 2009 -[Killer]- ###
##################################################
### If you use DO NOT REMOVE THIS !!! Do not   ###
### claim you made this, and/or redistribute   ###
##################################################


## import the random module
## Make sure you have python 2.5.2
## installed to make this work.
import random, bge


# get the controller and the owner
cont = bge.logic.getCurrentController()
own = cont.owner

# get the keyboard sensor called "space"
space = cont.sensors["space"]

# consult to the startup script
mult = bge.logic.multiplier

# set the min value for the attack
min = 10
# set the max value for the attack
max = 20


# if the space (attack) button is pushed
# and you have more than 0.000001 health...
if space.positive and own['health'] >= 0.0000001:
	# generate a random int value between
	# the min variable and the max variable...
	damage = random.randint(min,max)
	# take the damage from the health
	own['health'] -= damage

	# this uses the previously defines multiplier
	# to generate a "local" number to remove from
	# the ipo.
	own['ipo'] -= damage*mult
	
	# this handles if the health gets lower than
	# 0 (ie: if the health is 2 and you attack
	# with more than 2 damage and it makes is negative...
	if own['health'] <= 0:
		# set both the health and ipo to 0
		own['health'] = 0
		own['ipo'] = 0