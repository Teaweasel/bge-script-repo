##################################################
### Awesome Damage Script! ### 2009 -[Killer]- ###
##################################################
### If you use DO NOT REMOVE THIS !!! Do not   ###
### claim you made this, and/or redistribute   ###
##################################################

import bge
own = bge.logic.getCurrentController().owner


# this gets the multiplier value from the full
# health to the max health. ie: if the max health
# is 500 and the max ipo is 1000 the multiplier
# is set to 2, this means when 10 damage is done
# it takes 20 from the ipo.
bge.logic.multiplier = 1000/own['full']
# this fills up the health bar.
own['health'] = own['full']