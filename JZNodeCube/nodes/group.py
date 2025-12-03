from NodeGraphQt import  GroupNode, NodeGraph, BaseNode
from NodeGraphQt.qgraphics.node_base import NodeItem
from .basic import BaseNode2

class GroupNode2(BaseNode2, GroupNode):
    def __init__(self):
        super().__init__()
    
    def __getattr__(self, name):
        try:
            return getattr(super(BaseNode2, self), name)
        except AttributeError:
            return getattr(super(GroupNode, self), name)

class JZ8P2615(GroupNode2):
    __identifier__ = 'group'
    NODE_NAME = 'JZ8P2615'

    def __init__(self):
        super(JZ8P2615, self).__init__()
        self.set_color(50, 8, 25)
        
        self.add_bothway('P1', 'left')
        self.add_bothway('P2', 'right')