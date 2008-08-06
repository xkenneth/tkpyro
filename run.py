import pdb
import sys
from tkpyro.nodes import assemble
from tkpyro.helper import call_scripts

from lxml import etree

try:
    filename = sys.argv[1]
except IndexError:
    print "I....uhhh....need a file. :)"
    sys.exit()

tree = etree.fromstring(file(filename,'r').read())

#assemble the node tree

#assemble the canvas elements
canvas = assemble(tree)

#call all of the scripts
call_scripts(canvas)

#and loop!
canvas.master.mainloop()
