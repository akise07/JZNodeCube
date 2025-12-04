from NodeGraphQt import  GroupNode, NodeGraph, BaseNode
from NodeGraphQt.qgraphics.node_base import NodeItem
from NodeGraphQt.base.port import Port
from NodeGraphQt.constants import NodePropWidgetEnum, PortTypeEnum
from enum import Enum
from NodeGraphQt.errors import (
    PortError,
    PortRegistrationError,
    NodeWidgetError
)

class PortTypeEnum2(Enum):
    IN = 'in'
    OUT = 'out'
    BOTH = 'both'

class BaseNode2(BaseNode):
    def __init__(self, qgraphics_item=None):
        super(BaseNode, self).__init__(qgraphics_item or NodeItem)  # 调用父类的构造函数，如果未提供qgraphics_item则使用NodeItem
        self._inputs = []
        self._outputs = []
        self._bothways = []
    
    def bothways(self):
        return {p.name(): p for p in self._bothways}
    
    def add_bothway(self, name='bothway', direction='left', multi_bothway=True, display_name=True,
                color=None, locked=False, painter_func=None):
        if name in self.bothways().keys():
            raise PortRegistrationError(
                'port name "{}" already registered.'.format(name))
        port_args = [name, multi_bothway, display_name, locked]
        if painter_func and callable(painter_func):
            port_args.append(painter_func)
        if direction == 'left':
            view = self.view.add_input(*port_args)
        elif direction == 'right':
            view = self.view.add_output(*port_args)
            
        if color:
            view.color = color
            view.border_color = [min([255, max([0, i + 80])]) for i in color]

        port = Port(self, view)
        # port.model.type_ = PortTypeEnum2.BOTH.value
        port.model.name = name
        port.model.display_name = display_name
        port.model.multi_connection = multi_bothway
        port.model.locked = locked
        if direction == 'left':
            port.model.type_ = PortTypeEnum.IN.value
            self._inputs.append(port)
            self.model.inputs[port.name()] = port.model
        elif direction == 'right':
            port.model.type_ = PortTypeEnum.OUT.value
            self._outputs.append(port)
            self.model.outputs[port.name()] = port.model
        
        return port
    

class SimpleNode(BaseNode):
    __identifier__ = 'basic'
    NODE_NAME = 'SimpleNode'
    
    def __init__(self):
        super(SimpleNode, self).__init__()
        self.add_input('Input')
        self.add_output('Output')
        items = ['apples', 'bananas', 'pears', 'mangos', 'oranges']
        self.add_combo_menu('my_list', 'My List', items)

class 端口高电平(BaseNode):
    __identifier__ = 'basic'
    NODE_NAME = '端口高电平'
    
    def __init__(self):
        super(端口高电平, self).__init__()
        self.add_input('Input')