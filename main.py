import JZNodeCube, signal, sys, os
from pathlib import Path

# from PySide2 import QtCore, QtWidgets
from JZNodeCube import *
from Qt import QtCore, QtWidgets # type: ignore
from NodeGraphQt import NodeGraph, BaseNode, PropertiesBinWidget

BASE_PATH = Path(__file__).parent.resolve()

def main():
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    app = QtWidgets.QApplication([])
    main_window = QtWidgets.QMainWindow()
    main_window.setWindowTitle("JZNodeCube")
    main_window.resize(1400, 800)

    graph = NodeGraph()

    graph_widget = graph.widget
    main_window.setCentralWidget(graph_widget)

    properties_widget = PropertiesWidget()
    compile_widget = CompileWidget()

    # properties_bin = PropertiesBinWidget(node_graph=graph, parent=main_window)
    sidebar_manager = CubeSidebar(graph, properties_widget, compile_widget)
    dock_widget = QtWidgets.QDockWidget("节点属性", main_window)
    dock_widget.setWidget(sidebar_manager)
    dock_widget.setAllowedAreas(QtCore.Qt.RightDockWidgetArea | QtCore.Qt.LeftDockWidgetArea)
    main_window.addDockWidget(QtCore.Qt.RightDockWidgetArea, dock_widget)
    dock_widget.resize(300, 800)

    toolbar_manager = CubeToolbar(main_window, graph)

    # graph_widget.resize(1100, 800)
    # graph_widget.setWindowTitle("JZNodeCube")
    graph.register_node(basic.SimpleNode)
    graph.register_node(ic.JZ8P2615)

    simple_node = graph.create_node('basic.SimpleNode')
    JZ8P2615_node = graph.create_node('ic.JZ8P2615')
    # graph.expand_group_node(JZ8P2615_node)
    
    # properties_bin = PropertiesBinWidget(node_graph=graph, parent=graph_widget)
    # properties_bin.setWindowFlags(QtCore.Qt.Tool)

    # def display_properties_bin(node):
    #     if not properties_bin.isVisible():
    #         properties_bin.show()

    # wire function to "node_double_clicked" signal.
    # graph.node_double_clicked.connect(display_properties_bin)

    double_clicked = DoubleClicked(graph)
    graph.node_double_clicked.connect(lambda node: double_clicked.onDoubleClick(node))
    node_selected = NodeSelected(graph, properties_widget)
    graph.node_selected.connect(lambda node: node_selected.onNodeSelected(node))
    
    graph.fit_to_selection()
    hotkey_path = Path(BASE_PATH, 'JZNodeCube', 'hotkeys.json')
    graph.set_context_menu_from_file(hotkey_path, 'graph')

    graph.auto_layout_nodes()
    # graph_widget.show()
    # graph.show()
    graph.load_session('test.json')
    main_window.show()
    if hasattr(app, 'exec_'):
        return app.exec_()
    else:
        return app.exec()  

if __name__ == '__main__':
    main()