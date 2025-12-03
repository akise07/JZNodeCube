def show_save_message(graph):
    """
    在屏幕下方中心显示黄色"保存成功"消息，2秒后消失
    """
    from Qt import QtCore, QtWidgets # type: ignore
    
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
    
    # 创建单次定时器
    timer = QtCore.QTimer()
    timer.setSingleShot(True)
    timer.timeout.connect(hide_message)
    timer.start(2000)  # 2秒后执行

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

def save_session(graph):
    """
    Prompts a file save dialog to serialize a session if required.
    """
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


