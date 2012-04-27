################################################
##### Simple Portal ##### -[Killer]- ###########
### Do not remove this header from the script###
################################################

import bge

#Get the controller that activated the script
cont = bge.logic.getCurrentController()
#Get the owner of the controller
own = cont.owner

# This loads the empty that the cube will exit out of
warppoint = bge.logic.getCurrentScene().objects["Empty"]

# This gets the collision sensor
warp = cont.sensors["warp"]



# Get the position of the portal exit
warpto = warppoint.position
# Get the orientation of the portal exit
warporient = warppoint.orientation





# if the cube collides with the entrance...
if warp.positive:
	# Set the position of the cube to the position of
	# the portal exit
	own.position = warpto
	# Set the orientation of the cube to the portal's
	# orientation.
	own.orientation = warporient
	# When exiting the grav will reset, so we add this
	# so it looks like the motion never stopped.
	own.setLinearVelocity([0,0,-4.9],1)
