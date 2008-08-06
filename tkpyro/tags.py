#builtin types
import pdb
import Tkinter
import Pmw
import re

from helper import koi, correct_indentation, not_koi, ignorable, grid_keys, evaluate_constraints

from nodes import assemble

class _obj:
    def __init__(self):
        self.child_nodes = []
    
class _visible_obj(_obj):
    def show(self):
        if bool(self.tag.get('pack')):
            self.pack()
        else:
            self.widget.grid(koi(self.tag,grid_keys))

class Script(_obj):
    __tag__ = 'script'
    def __call__(self,event=None):
        exec correct_indentation(self.tag.text)
    def construct(self):
        exec correct_indentation(self.tag.text)

class Event(Script):
    __tag__ = 'event'
    def construct(self):
        self.parent.widget.bind('<'+self.tag.get('on')+'>',self,evaluate_constraints(self,not_koi(self.tag,ignorable)))

class Canvas(_visible_obj):
    __tag__ = 'canvas'
    def construct(self):
        self.master = Tkinter.Tk()
        self.widget = self.master

class Text(_visible_obj):
    __tag__ = 'text'
    def construct(self):
        self.widget = Tkinter.Label(self.parent.widget,evaluate_constraints(self,not_koi(self.tag,ignorable)))

class Entry(_visible_obj):
    __tag__ = 'entry'
    def construct(self):
        self.widget = Tkinter.Entry(self.parent.widget,evaluate_constraints(self,not_koi(self.tag,ignorable)))

class Button(_visible_obj):
    __tag__ = 'button'

    def construct(self):
        self.widget = Tkinter.Button(self.parent.widget,evaluate_constraints(self,not_koi(self.tag,ignorable)))

class Frame(_visible_obj):
    __tag__ = 'frame'
    
    def construct(self):
        self.widget = Tkinter.Frame(self.parent.widget,evaluate_constraints(self,not_koi(self.tag,ignorable)))

class NoteBook(_visible_obj):
    __tag__ = 'notebook'
    
    def construct(self):
        self.widget = Pmw.NoteBook(self.parent.widget)

    def late(self):
        self.widget.setnaturalsize()

class Page(_obj):
    __tag__ = 'page'
    
    def construct(self):

        self.widget = self.parent.widget.add(self.tag.get('title'))

class Replicate(_obj):
    __tag__ = 'replicate'
    
    def construct(self):
        for data in eval(self.tag.get('over')):
            for child_node in self.tag:
                new_node = assemble(child_node,self.parent,data=data)
                
tag_names = [Canvas,Text,Button,Frame,Script,Event,NoteBook,Page,Replicate,Entry]



                            
                            
