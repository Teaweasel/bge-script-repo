import bge
cont = bge.logic.getCurrentController()
own = cont.owner

click = own.sensors['click']
mposi = own.sensors['mposi']



sc = bge.logic.getCurrentScene()
obl = sc.objects


if click.positive:
    x,y,z = mposi.hitPosition
    ox,oy,oz = own.position
    if own['set'] == False:
        own.position = [x,y,0]
        own['set'] = True
    else:
        own.scaling = [(x-ox)/2,-(y-oy)/2,0]
        bounds = {'top':oy,
                    'bottom':y,
                    'left':ox,
                    'right':x}
        
        for i in obl:
            try:
                if i['selectable']:
                    if (i.position.x > bounds['left'] and i.position.x < bounds['right'] and i.position.y > bounds['bottom'] and i.position.y < bounds['top']) or (i.position.x < bounds['left'] and i.position.x > bounds['right'] and i.position.y < bounds['bottom'] and i.position.y > bounds['top']) or (i.position.x < bounds['left'] and i.position.x > bounds['right'] and i.position.y > bounds['bottom'] and i.position.y < bounds['top']) or (i.position.x > bounds['left'] and i.position.x < bounds['right'] and i.position.y < bounds['bottom'] and i.position.y > bounds['top']):

                        i.scaling = [2,2,2]
                    else:
                        i.scaling = [1,1,1] 
                        
            except:
                pass
            
              

else:
    own['set'] = False
