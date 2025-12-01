from NodeGraphQt import NodeGraph, BaseNode

class SimpleNode(BaseNode):
    __identifier__ = 'com.example'
    NODE_NAME = 'Simple Node'
    
    def __init__(self):
        super(SimpleNode, self).__init__()
        self.add_input('Input')
        self.add_output('Output')