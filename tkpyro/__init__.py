from lxml import etree
from tkpyro.nodes import assemble
from tkpyro.helper import call_scripts

def run(filename):
    tree = etree.fromstring(file(filename,'r').read())
    
    #assemble the canvas elements
    canvas = assemble(tree)
 
    #call all of the scripts
    call_scripts(canvas)
 
    #and loop!
    canvas.master.mainloop()
        

