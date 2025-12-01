from NodeGraphQt import NodeGraph, BaseNode
from NodeGraphQt.qgraphics.node_base import NodeItem

class BaseNode(BaseNode):
    def __init__(self, qgraphics_item=None):
        super(BaseNode, self).__init__(qgraphics_item or NodeItem)
        self._inputs = []
        self._outputs = []
        self._bothways = []
    
    def bothways(self):
        return {p.name(): p for p in self._bothways}
    
    def add_input(self, name='bothway', multi_input=False, display_name=True,
                color=None, locked=False, painter_func=None):
        if name in self.outputs().keys():
            raise PortRegistrationError(
                'port name "{}" already registered.'.format(name))

        port_args = [name, multi_input, display_name, locked]
        if painter_func and callable(painter_func):
            port_args.append(painter_func)
        view = self.view.add_input(*port_args)

        if color:
            view.color = color
            view.border_color = [min([255, max([0, i + 80])]) for i in color]

        port = Port(self, view)
        port.model.type_ = PortTypeEnum.IN.value
        port.model.name = name
        port.model.display_name = display_name
        port.model.multi_connection = multi_input
        port.model.locked = locked
        self._inputs.append(port)
        self.model.inputs[port.name()] = port.model
        return port
    

class SimpleNode(BaseNode):
    __identifier__ = 'basic'
    NODE_NAME = 'Simple Node'
    
    def __init__(self):
        super(SimpleNode, self).__init__()
        self.add_input('Input')
        self.add_output('Output')
        items = ['apples', 'bananas', 'pears', 'mangos', 'oranges']
        self.add_combo_menu('my_list', 'My List', items)