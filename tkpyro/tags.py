#builtin types
import pdb
import Tkinter

from helper import koi, correct_indentation, not_koi, ignorable, grid_keys

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
    def __call__(self,event):
        exec correct_indentation(self.tag.text)

class Event(Script):
    __tag__ = 'event'
    def construct(self):
        self.parent.widget.bind('<'+self.tag.get('on')+'>',self,not_koi(self.tag,ignorable))

class Canvas(_visible_obj):
    __tag__ = 'canvas'
    def construct(self):
        self.master = Tkinter.Tk()
        self.widget = self.master

class Text(_visible_obj):
    __tag__ = 'text'
    def construct(self):
        self.widget = Tkinter.Label(self.parent.widget,not_koi(self.tag,ignorable))

class Button(_visible_obj):
    __tag__ = 'button'

    def construct(self):
        self.widget = Tkinter.Button(self.parent.widget,not_koi(self.tag,ignorable))

class Frame(_visible_obj):
    __tag__ = 'frame'
    
    def construct(self):
        self.widget = Tkinter.Frame(self.parent.widget,not_koi(self.tag,ignorable))

tags = [Canvas,Text,Button,Frame,Script,Event]
    
