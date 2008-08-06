import sys
import pdb

from helper import construct_class, evaluate_constraints

#assemble objects recursively
canvas = None
def assemble(tree,parent=None,data=None):
    global canvas
    
    new_node = None

    #if we need to stop traversing for any reason, mostly for replicate nodes
    stop = False

    #if it's the first call and we have no parent
    if parent is None:
        #construct the canvas
        canvas = construct_class(tree) 
        canvas.tag = tree
        canvas.construct()
        parent = canvas
        
    else:
        #else construct the class
        new_node = construct_class(tree)
        if not new_node:
            return
        
        #we don't want to construct the child nodes of a replicate tag in the normal manner, so we don't traverse them
        if new_node.tag.tag == 'replicate':
            stop = True

        #set it's parent
        new_node.parent = parent

        #attach the data if it's been replicated
        if data:
            new_node.data = data
        #construct it
        if hasattr(new_node,'construct'):
            new_node.construct()

        #if it's a visible node, show it
        if hasattr(new_node,'show'):
            new_node.show()
        
        #attach the canvas to each node
        new_node.canvas = canvas

        #if it has a name, create it as an attribute on the parent
        name = new_node.tag.get('name')
        
        if name:
            name = evaluate_constraints(new_node,name)
            
            if hasattr(parent,name):
                raise ValueError('Name already taken!')
            parent.__dict__[name] = new_node

        #if it has an ID as well, assign it to the parent
        id = new_node.tag.get('id')
        if id:
            if hasattr(canvas,id):
                raise ValueError('ID Already Taken!')
            canvas.__dict__[id] = new_node

        #append it to it's parent
        parent.child_nodes.append(new_node)
        
    if not stop:
        for child in tree:
            #work on all of the children
            if new_node is None:
                new_node = parent
            assemble(child,new_node)

    return canvas


