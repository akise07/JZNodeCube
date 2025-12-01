from NodeGraphQt import NodeGraph, BaseNode

class SimpleNode(BaseNode):
    __identifier__ = 'basic'
    NODE_NAME = 'Simple Node'
    
    def __init__(self):
        super(SimpleNode, self).__init__()
        self.add_input('Input')
        self.add_output('Output')
        items = ['apples', 'bananas', 'pears', 'mangos', 'oranges']
        self.add_combo_menu('my_list', 'My List', items)