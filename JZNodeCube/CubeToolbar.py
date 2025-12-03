from Qt import QtCore, QtWidgets # type: ignore

class CubeToolbar():
    
    def __init__(self, main_window, graph=None):
        """
        初始化工具栏
        
        Args:
            main_window: 主窗口对象
            graph: 节点图对象，可选
        """
        self.main_window = main_window
        self.graph = graph
        self.toolbar = None
        
        # 只创建工具栏，不创建状态栏
        self.create_toolbar()
    
    def create_toolbar(self):
        """创建工具栏"""
        # 创建主工具栏
        self.toolbar = self.main_window.addToolBar("主工具栏")
        self.toolbar.setMovable(False)  # 固定工具栏位置
        
        # 添加编译按钮
        compile_action = QtWidgets.QAction("编译", self.main_window)
        compile_action.setStatusTip("编译当前节点图")
        compile_action.triggered.connect(self.compile_graph)
        self.toolbar.addAction(compile_action)
        
        # 添加分隔符
        self.toolbar.addSeparator()
        
        # 添加关于按钮
        about_action = QtWidgets.QAction("关于", self.main_window)
        about_action.setStatusTip("关于JZNodeCube")
        about_action.triggered.connect(self.show_about)
        self.toolbar.addAction(about_action)
        
        # 添加帮助按钮
        help_action = QtWidgets.QAction("帮助", self.main_window)
        help_action.setStatusTip("获取帮助信息")
        help_action.triggered.connect(self.show_help)
        self.toolbar.addAction(help_action)
        
        return self.toolbar
    
    def set_graph(self, graph):
        """设置节点图对象"""
        self.graph = graph
    
    def compile_graph(self):
        """编译当前节点图"""
        # 获取所有节点
        nodes = []
        if self.graph:
            nodes = self.graph.all_nodes()
        
        # 这里添加实际的编译逻辑
        # 例如：将节点图转换为代码或其他格式
        
        # 显示编译结果对话框
        QtWidgets.QMessageBox.information(
            self.main_window, 
            "编译结果", 
            f"成功编译节点图！\n处理了 {len(nodes)} 个节点。\n\n注意：这里只是示例编译，实际编译逻辑需要根据项目需求实现。"
        )
    
    def show_about(self):
        """显示关于对话框"""
        about_text = """
        <h2>JZNodeCube</h2>
        <p>版本: 1.0.0</p>
        <p>一个基于NodeGraphQt的可视化节点编辑器</p>
        <p>用于创建和编辑节点图</p>
        <br>
        <p>版权所有 © 2023</p>
        """
        
        QtWidgets.QMessageBox.about(self.main_window, "关于 JZNodeCube", about_text)
    
    def show_help(self):
        """显示帮助对话框"""
        help_text = """
        <h2>JZNodeCube 使用帮助</h2>
        
        <h3>基本操作</h3>
        <ul>
        <li><b>创建节点:</b> 右键点击图形区域，从菜单中选择节点类型</li>
        <li><b>连接节点:</b> 从一个端口的输出拖动到另一个端口的输入</li>
        <li><b>选择节点:</b> 单击节点进行选择</li>
        <li><b>移动节点:</b> 拖动节点到新位置</li>
        <li><b>删除节点:</b> 选中节点后按Delete键</li>
        </ul>
        
        <h3>工具栏功能</h3>
        <ul>
        <li><b>编译:</b> 将当前节点图编译为目标格式</li>
        <li><b>关于:</b> 查看应用程序信息</li>
        <li><b>帮助:</b> 显示此帮助信息</li>
        </ul>
        
        <h3>快捷键</h3>
        <ul>
        <li><b>Delete:</b> 删除选中的节点</li>
        <li><b>Ctrl+Z:</b> 撤销操作</li>
        <li><b>Ctrl+Y:</b> 重做操作</li>
        </ul>
        """
        
        msg = QtWidgets.QMessageBox(self.main_window)
        msg.setWindowTitle("帮助")
        msg.setTextFormat(QtCore.Qt.RichText)
        msg.setText(help_text)
        msg.exec_()