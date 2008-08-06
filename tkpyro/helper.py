#return the keys (attributes) of interest from a particular tag
import re
import unittest
import pdb

tab_re = re.compile('\s*')

global_keys = ['name','id']
grid_keys = ['row','column','columnspan','rowspan']
pack_keys = ['pack']

ignorable = global_keys

ignorable.extend(grid_keys)
ignorable.extend(pack_keys)

def call_scripts(node,parent=None):
    if parent is None:
        parent = node
    else:
        if node.__tag__ == 'script':
            node()
    for sub_node in node.child_nodes:
        call_scripts(sub_node,parent)

def not_koi(tag,keys):
    assembled = {}
    for attribute in tag.keys():
        try:
            keys.index(attribute)
        except ValueError:
            assembled[attribute] = tag.get(attribute)

    return assembled

def koi(tag,keys):
    assembled = {}
    for k in keys:
        val = tag.get(k)

        try:
            if val.lower() == 'true' or val.lower() == 'false':
                val = bool(val)
        except AttributeError:
            pass

        try:
            val = int(val)
        except TypeError:
            pass
        assembled[k] = val

    return assembled
        
    
def correct_indentation(script):
    #split by line, take the first empty line out
    lines = script.split('\n')
    
    #get rid of the first line if it's empty
    if lines[0] == '':
        lines = lines[1:]
        
    #find out the number of tabs at the front of the line
    num_tabs = len(tab_re.match(lines[0]).group())
    
    proper_script = ''
    #for each line, remove the number of tabs
    for line in lines:
        proper_script += line[num_tabs:] + '\n'

    return proper_script

if __name__ == '__main__':
    class correct_indentation_tests(unittest.TestCase):
        def setUp(self):
            self.test_string = "\n\tif True:\n\t\tprint 'Yay!'"
            self.correct_string = "if True:\n\tprint 'Yay!'\n"
        def testOne(self):
            self.failUnlessEqual(correct_indentation(self.test_string),self.correct_string)
    
    
    unittest.main()
