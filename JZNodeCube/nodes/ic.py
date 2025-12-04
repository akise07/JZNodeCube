from NodeGraphQt import  GroupNode, NodeGraph, BaseNode
from NodeGraphQt.qgraphics.node_base import NodeItem
from .group import GroupNode2

class JZ8P2615(GroupNode2):
    __identifier__ = 'ic'
    NODE_NAME = 'JZ8P2615'

    def __init__(self):
        super(JZ8P2615, self).__init__()
        self.set_color(50, 8, 25)
        
        # self.add_bothway('P1', 'left')
        # self.add_bothway('P2', 'right')
        self.add_input('Ps1')
        # self.add_output('P2')