import pdb
from lxml import etree
from nodes import assemble
from tkpyro.helper import call_scripts, call_late
from tags import Canvas

def run(filename):
    tree = etree.fromstring(file(filename,'r').read())
    
    

    #set up the imports
    import tags
    if tree.get('import'):
        for module in tree.get('import').split(','):
            tags.__dict__[module.split('.')[0]] = __import__(module)

    #create the canvas object
    canvas = Canvas()
    #construct it
    canvas.construct()
    #make sure that it's global to the nodes module for node construction
    nodes.canvas = canvas

    #make the canvas global
    tags.__dict__['canvas'] = canvas
    
    #assemble the canvas elements
    for child in tree:
        assemble(child,canvas)

    #call all of the scripts
    #call_scripts(canvas)
    call_late(canvas)

    #and loop!
    canvas.master.mainloop()
        

