import pdb
from lxml import etree
from nodes import assemble
from tkpyro.helper import call_scripts

def run(filename):
    tree = etree.fromstring(file(filename,'r').read())
    
    #assemble the canvas elements
    canvas = assemble(tree)

    #set up the imports
    import tags
    if canvas.tag.get('import'):
        for module in canvas.tag.get('import').split(','):
            tags.__dict__[module.split('.')[0]] = __import__(module)
    #make the canvas global
    tags.__dict__['canvas'] = canvas

    #call all of the scripts
    call_scripts(canvas)

    #and loop!
    canvas.master.mainloop()
        

