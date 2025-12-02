from NodeGraphQt import  GroupNode, NodeGraph, BaseNode
from NodeGraphQt.qgraphics.node_base import NodeItem

class JZ8P2615(GroupNode):
    __identifier__ = 'group'
    NODE_NAME = 'JZ8P2615'

    def __init__(self):
        super(JZ8P2615, self).__init__()
        self.set_color(50, 8, 25)
        
        self.add_input('in')
        self.add_output('out')