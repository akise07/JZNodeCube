from NodeGraphQt import  GroupNode, NodeGraph, BaseNode, SubGraph
from NodeGraphQt.qgraphics.node_base import NodeItem
from NodeGraphQt.constants import NodePropWidgetEnum, PortTypeEnum
from .basic import BaseNode2

def get_node_by_port(self, port):
        func_type = {
            PortTypeEnum.IN.value: self.get_input_port_nodes(),
            PortTypeEnum.OUT.value: self.get_output_port_nodes()
        }
        # print(port.type_())
        # print(func_type)
        for n in func_type.get(port.type_(), []):
            if port == n.parent_port:
                return n

SubGraph.get_node_by_port = get_node_by_port

class GroupNode2(BaseNode2, GroupNode):
    def __init__(self):
        super().__init__()
    
    def delete_input(self, port):
        if type(port) in [int, str]:
            port = self.get_input(port)
            if port is None:
                return

        if self.is_expanded:
            sub_graph: SubGraph = self.get_sub_graph()
            port_node = sub_graph.get_node_by_port(port)
            if port_node:
                sub_graph.remove_node(port_node, push_undo=False)

        super(GroupNode, self).delete_input(port)
    
    def __getattr__(self, name):
        try:
            return getattr(super(BaseNode2, self), name)
        except AttributeError:
            return getattr(super(GroupNode, self), name)