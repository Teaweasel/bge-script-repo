########### UV SCROLL SCRIPT ##################33
##### -[Killer]- #########

import bge

#get all the mesh info
cont = bge.logic.getCurrentController() 
own = cont.owner 
mesh = own.meshes[0] 
array = mesh.getVertexArrayLength(0)
#...

# Variables
speed = own['speed']
axis = own['axis']
#...

# find what axis to move on
if axis == "x":
	axis = 0
if axis == "y":
	axis = 1
#...
	
	
# Now let's move the UV
for v in range(0,array):
	vertex = mesh.getVertex(0,v)
	UV = vertex.getUV()
	UV[axis] = UV[axis]+speed
	vertex.setUV(UV)
#...