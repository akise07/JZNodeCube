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
    
    # def delete_input(self, port):
    #     if type(port) in [int, str]:
    #         port = self.get_input(port)
    #         if port is None:
    #             return

    #     if self.is_expanded:
    #         sub_graph: SubGraph = self.get_sub_graph()
    #         port_node = sub_graph.get_node_by_port(port)
    #         if port_node:
    #             sub_graph.remove_node(port_node, push_undo=False)

    #     super(GroupNode, self).delete_input(port)
    
    # def delete_output(self, port):
    #     if type(port) in [int, str]:
    #         port = self.get_output(port)
    #         if port is None:
    #             return

    #     if self.is_expanded:
    #         sub_graph = self.get_sub_graph()
    #         port_node = sub_graph.get_node_by_port(port)
    #         if port_node:
    #             sub_graph.remove_node(port_node, push_undo=False)

    #     super(GroupNode, self).delete_output(port)
    
    def set_ports(self, port_data):
        if not self.port_deletion_allowed():
            raise PortError(
                'Ports cannot be set on this node because '
                '"set_port_deletion_allowed" is not enabled on this node.')
        
        for port in self._inputs:
            self.delete_input(port)
            # self._view.delete_input(port.view)
            port.model.node = None
        for port in self._outputs:
            self.delete_output(port)
            # self._view.delete_output(port.view)
            port.model.node = None
        self._inputs = []
        self._outputs = []
        self._model.outputs = {}
        self._model.inputs = {}

        [self.add_input(name=port['name'],
                        multi_input=port['multi_connection'],
                        display_name=port['display_name'],
                        locked=port.get('locked') or False)
        for port in port_data['input_ports']]
        [self.add_output(name=port['name'],
                        multi_output=port['multi_connection'],
                        display_name=port['display_name'],
                        locked=port.get('locked') or False)
        for port in port_data['output_ports']]
        self._view.draw_node()
    
    
    def __getattr__(self, name):
        try:
            return getattr(super(BaseNode2, self), name)
        except AttributeError:
            return getattr(super(GroupNode, self), name)