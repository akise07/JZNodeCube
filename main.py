import sys

from pathlib import Path
from PySide2 import QtWidgets, QtCore
from NodeGraphQt import NodeGraph, BaseNode
from JZNodeCube import *

BASE_PATH = Path(__file__).parent.resolve()

def main():
    app = QtWidgets.QApplication(sys.argv)
    graph = NodeGraph()
    graph.register_node(nodes.SimpleNode)
    node = graph.create_node('com.example.SimpleNode')
    
    graph.set_zoom(2)
    graph.fit_to_selection()
    hotkey_path = Path(BASE_PATH, 'JZNodeCube', 'hotkeys.json')
    graph.set_context_menu_from_file(hotkey_path, 'graph')

    graph.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()