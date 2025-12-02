import JZNodeCube, signal
from pathlib import Path
# from PySide2 import QtWidgets, QtCore

from PySide2 import QtCore, QtWidgets
# from Qt import QtCore, QtWidgets
from NodeGraphQt import NodeGraph, BaseNode, PropertiesBinWidget
from JZNodeCube import *

BASE_PATH = Path(__file__).parent.resolve()

def main():
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    app = QtWidgets.QApplication([])
    graph = NodeGraph()
    graph_widget = graph.widget
    graph_widget.resize(1100, 800)
    graph_widget.setWindowTitle("JZNodeCube")

    graph.register_node(basic.SimpleNode)
    graph.register_node(group.JZ8P2615)
    
    simple_node = graph.create_node('basic.SimpleNode')
    JZ8P2615_node = graph.create_node('group.JZ8P2615')
    # graph.expand_group_node(JZ8P2615_node)
    
    properties_bin = PropertiesBinWidget(node_graph=graph, parent=graph_widget)
    properties_bin.setWindowFlags(QtCore.Qt.Tool)

    # example show the node properties bin widget when a node is double-clicked.
    def display_properties_bin(node):
        if not properties_bin.isVisible():
            properties_bin.show()

    # wire function to "node_double_clicked" signal.
    # graph.node_double_clicked.connect(display_properties_bin)
    double_clicked = DoubleClicked(graph)
    graph.node_double_clicked.connect(lambda node: double_clicked.onDoubleClick(node))
    graph.fit_to_selection()
    hotkey_path = Path(BASE_PATH, 'JZNodeCube', 'hotkeys.json')
    graph.set_context_menu_from_file(hotkey_path, 'graph')

    graph.auto_layout_nodes()
    # graph_widget.show()
    graph.show()
    if hasattr(app, 'exec_'):
        return app.exec_()
    else:
        return app.exec()  

if __name__ == '__main__':
    main()