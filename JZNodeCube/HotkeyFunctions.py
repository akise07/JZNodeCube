import threading, time
from NodeGraphQt import NodeGraph, SubGraph
from Qt import QtCore, QtWidgets # type: ignore
from NodeGraphQt.nodes.port_node import PortInputNode, PortOutputNode

def show_save_message(graph):
    # 获取主窗口 - 使用更可靠的方式
    widget = graph.widget
    main_window = widget
    # 向上查找主窗口
    while main_window.parent():
        main_window = main_window.parent()
    # 创建消息标签
    message_label = QtWidgets.QLabel("保存成功", main_window)
    message_label.setStyleSheet("""
        QLabel {
            background-color: rgba(255, 255, 0, 200);
            color: black;
            padding: 10px 20px;
            border-radius: 5px;
            font-weight: bold;
        }
    """)
    # 设置标签位置和大小
    message_label.adjustSize()
    x = (main_window.width() - message_label.width()) // 2
    y = main_window.height() - message_label.height() - 50  # 距离底部50像素
    message_label.move(x, y)
    message_label.show()
    
    # 设置定时器，2秒后隐藏并删除消息
    def hide_message():
        if message_label:
            message_label.hide()
            message_label.deleteLater()
    
    threading.Timer(2, hide_message).start()

# File
def open_session(graph):
    """
    Prompts a file open dialog to load a session.
    """
    current = graph.current_session()
    file_path = graph.load_dialog(current)
    if file_path:
        graph.load_session(file_path)

def save_session_as(graph):
    """
    Prompts a file save dialog to serialize a session.
    """
    current = graph.current_session()
    file_path = graph.save_dialog(current)
    if file_path:
        graph.save_session(file_path)

def save_session(graph: NodeGraph):
    """
    Prompts a file save dialog to serialize a session if required.
    """
    if isinstance(graph, SubGraph):
        for node in graph.all_nodes():
            if isinstance(node, PortInputNode):
                print(1)
            if isinstance(node, PortOutputNode):
                print(2)
        return
    current = graph.current_session()
    if current:
        graph.save_session(current)
        msg = 'Session layout saved:\n{}'.format(current)
        show_save_message(graph)
        # viewer = graph.viewer()
        # viewer.message_dialog(msg, title='Session Saved')
    else:
        save_session_as(graph)

# Edit
def zoom_in(graph):
    """
    Set the node graph to zoom in by 0.1
    """
    zoom = graph.get_zoom() + 0.1
    graph.set_zoom(zoom)

def zoom_out(graph):
    """
    Set the node graph to zoom in by 0.1
    """
    zoom = graph.get_zoom() - 0.2
    graph.set_zoom(zoom)

def copy_nodes(graph):
    """
    Copy nodes to the clipboard.
    """
    graph.copy_nodes()


def cut_nodes(graph):
    """
    Cut nodes to the clip board.
    """
    graph.cut_nodes()


def paste_nodes(graph):
    """
    Pastes nodes copied from the clipboard.
    """
    # by default the graph will inherite the global style
    # from the graph when pasting nodes.
    # to disable this behaviour set `adjust_graph_style` to False.
    graph.paste_nodes(adjust_graph_style=False)


def delete_nodes_and_pipes(graph):
    """
    Delete selected nodes and connections.
    """
    graph.delete_nodes(graph.selected_nodes())
    for pipe in graph.selected_pipes():
        pipe[0].disconnect_from(pipe[1])

def select_all_nodes(graph):
    """
    Select all nodes.
    """
    graph.select_all()


def clear_node_selection(graph):
    """
    Clear node selection.
    """
    graph.clear_selection()

# Nodes
def toggle_node_search(graph):
    """
    show/hide the node search widget.
    """
    graph.toggle_node_search()
