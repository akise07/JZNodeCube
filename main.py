import JZNodeCube, signal
from pathlib import Path
# from PySide2 import QtWidgets, QtCore
from Qt import QtCore, QtWidgets
from NodeGraphQt import NodeGraph, BaseNode, PropertiesBinWidget
from JZNodeCube import *


BASE_PATH = Path(__file__).parent.resolve()

def main():
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    app = QtWidgets.QApplication([])
    graph = NodeGraph()
    graph.register_node(basic.SimpleNode)
    node = graph.create_node('basic.SimpleNode')
    
    graph_widget = graph.widget
    graph_widget.resize(1100, 800)
    graph_widget.setWindowTitle("JZNodeCube")

    properties_bin = PropertiesBinWidget(node_graph=graph, parent=graph_widget)
    properties_bin.setWindowFlags(QtCore.Qt.Tool)

    # example show the node properties bin widget when a node is double-clicked.
    def display_properties_bin(node):
        if not properties_bin.isVisible():
            properties_bin.show()

    # wire function to "node_double_clicked" signal.
    # graph.node_double_clicked.connect(display_properties_bin)
    graph.node_double_clicked.connect(lambda node: print(node.NODE_NAME))
    graph.fit_to_selection()
    hotkey_path = Path(BASE_PATH, 'JZNodeCube', 'hotkeys.json')
    graph.set_context_menu_from_file(hotkey_path, 'graph')

    # graph.auto_layout_nodes()
    # graph.show()
    graph_widget.show()
    app.exec()

if __name__ == '__main__':
    main()