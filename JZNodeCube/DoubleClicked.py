from PySide2 import QtCore, QtWidgets
from NodeGraphQt import NodeGraph, BaseNode, PropertiesBinWidget

class DoubleClicked():
    def __init__(self, graph: NodeGraph):
        self.graph = graph

    def create_subgraph(self, node):
        node_name = f'{node.__identifier__}.{node.NODE_NAME}'
        # node = self.graph._node_factory.create_node_instance(node_name)
        self.graph.get_node_by_name(node_name)
        if node:
            self.graph.expand_group_node(node)

    def onDoubleClick(self, node):
        self.create_subgraph(node)
    
    