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