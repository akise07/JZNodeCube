from Qt import QtCore, QtWidgets, QtGui # type: ignore
from NodeGraphQt import NodeGraph

class PropertiesWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.is_locked = False
        self.setFixedWidth(300)
        self.setup_ui()
        
    def setup_ui(self):
        layout = QtWidgets.QVBoxLayout(self)
        
    def clear_properties(self):
        layout = self.layout()
        while layout.count():
            item = layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
            elif item.layout():
                while item.layout().count():
                    sub_item = item.layout().takeAt(0)
                    if sub_item.widget():
                        sub_item.widget().deleteLater()
    
    def update_data(self, node):
        if self.is_locked:
            return None
        self.clear_properties()
        layout = self.layout()
        if node.__identifier__ == 'ic':
            # 添加标题
            title = QtWidgets.QLabel("节点属性")
            title.setStyleSheet("font-weight: bold; font-size: 14px; padding: 5px;")
            layout.addWidget(title)

            # 添加右侧锁定按钮
            lock_btn = QtWidgets.QPushButton("Lock")
            lock_btn.setFixedSize(24*3, 24)
            lock_btn.setToolTip("锁定侧边栏")
            def switch_lock():
                if self.is_locked:
                    self.is_locked = False
                    lock_btn.setText("Lock")
                else:
                    self.is_locked = True
                    lock_btn.setText("Locked")
            lock_btn.clicked.connect(lambda: switch_lock())

            # 将按钮放在右上角：先放一个水平布局，把标题和按钮包起来
            header_layout = QtWidgets.QHBoxLayout()
            header_layout.addWidget(title)
            header_layout.addStretch()
            header_layout.addWidget(lock_btn)
            header_layout.setContentsMargins(0, 0, 0, 0)
            layout.addLayout(header_layout)

            # 添加分隔线
            line = QtWidgets.QFrame()
            line.setFrameShape(QtWidgets.QFrame.HLine)
            line.setFrameShadow(QtWidgets.QFrame.Sunken)
            layout.addWidget(line)
            
            # 添加自定义属性行
            # 第一行：文本 + 勾选框
            row1_layout = QtWidgets.QHBoxLayout()
            label1 = QtWidgets.QLabel("启用功能")
            checkbox1 = QtWidgets.QCheckBox()
            row1_layout.addWidget(label1)
            row1_layout.addWidget(checkbox1)
            row1_layout.addStretch()
            layout.addLayout(row1_layout)
            
            # 第二行：文本 + 勾选框
            row2_layout = QtWidgets.QHBoxLayout()
            label2 = QtWidgets.QLabel("自动保存")
            checkbox2 = QtWidgets.QCheckBox()
            row2_layout.addWidget(label2)
            row2_layout.addWidget(checkbox2)
            row2_layout.addStretch()
            layout.addLayout(row2_layout)
            
            # 第三行：文本 + 勾选框
            row3_layout = QtWidgets.QHBoxLayout()
            label3 = QtWidgets.QLabel("显示网格")
            checkbox3 = QtWidgets.QCheckBox()
            checkbox3.setChecked(True)  # 默认选中
            row3_layout.addWidget(label3)
            row3_layout.addWidget(checkbox3)
            row3_layout.addStretch()
            layout.addLayout(row3_layout)
            
            # 第四行：文本 + 勾选框
            row4_layout = QtWidgets.QHBoxLayout()
            label4 = QtWidgets.QLabel("启用动画")
            checkbox4 = QtWidgets.QCheckBox()
            row4_layout.addWidget(label4)
            row4_layout.addWidget(checkbox4)
            row4_layout.addStretch()
            layout.addLayout(row4_layout)
            
            # 第五行：文本 + 勾选框
            row5_layout = QtWidgets.QHBoxLayout()
            label5 = QtWidgets.QLabel("调试模式")
            checkbox5 = QtWidgets.QCheckBox()
            row5_layout.addWidget(label5)
            row5_layout.addWidget(checkbox5)
            row5_layout.addStretch()
            layout.addLayout(row5_layout)
            
            # 添加弹性空间
            layout.addStretch()
            
            # 保存复选框引用以便后续访问
            self.checkboxes = {
                "enable_feature": checkbox1,
                "auto_save": checkbox2,
                "show_grid": checkbox3,
                "enable_animation": checkbox4,
                "debug_mode": checkbox5
            }
            
            # 连接信号
            # checkbox1.stateChanged.connect(self.on_enable_feature_changed)
            # checkbox2.stateChanged.connect(self.on_auto_save_changed)
            # checkbox3.stateChanged.connect(self.on_show_grid_changed)
            # checkbox4.stateChanged.connect(self.on_enable_animation_changed)
            # checkbox5.stateChanged.connect(self.on_debug_mode_changed)
        
class CompileWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedWidth(300)
        self.setup_ui()
        
    def setup_ui(self):
        layout = QtWidgets.QVBoxLayout(self)
        
        # 添加标题
        title = QtWidgets.QLabel("编译内容")
        title.setStyleSheet("font-weight: bold; font-size: 14px; padding: 5px;")
        layout.addWidget(title)
        
        # 添加分隔线
        line = QtWidgets.QFrame()
        line.setFrameShape(QtWidgets.QFrame.HLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)
        layout.addWidget(line)
        
        # 创建编译结果文本区域
        self.compile_output = QtWidgets.QTextEdit()
        self.compile_output.setReadOnly(True)
        self.compile_output.setFont(QtGui.QFont("Consolas", 9))
        layout.addWidget(self.compile_output)
        
        # 添加控制按钮区域
        button_layout = QtWidgets.QHBoxLayout()
        
        # 清空按钮
        clear_button = QtWidgets.QPushButton("清空")
        clear_button.clicked.connect(self.clear_output)
        button_layout.addWidget(clear_button)
        
        # 保存按钮
        save_button = QtWidgets.QPushButton("保存")
        save_button.clicked.connect(self.save_output)
        button_layout.addWidget(save_button)
        
        layout.addLayout(button_layout)
        
    def clear_output(self):
        """清空编译输出"""
        self.compile_output.clear()
        
    def save_output(self):
        """保存编译输出到文件"""
        options = QtWidgets.QFileDialog.Options()
        file_name, _ = QtWidgets.QFileDialog.getSaveFileName(
            self, "保存编译结果", "", "文本文件 (*.txt);;所有文件 (*)", options=options)
        
        if file_name:
            try:
                with open(file_name, 'w', encoding='utf-8') as f:
                    f.write(self.compile_output.toPlainText())
                QtWidgets.QMessageBox.information(self, "保存成功", f"编译结果已保存到: {file_name}")
            except Exception as e:
                QtWidgets.QMessageBox.critical(self, "保存失败", f"保存文件时出错: {str(e)}")
    
    def append_output(self, text, color=None):
        """添加文本到编译输出"""
        cursor = self.compile_output.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        
        if color:
            # 设置文本颜色
            char_format = QtGui.QTextCharFormat()
            char_format.setForeground(QtGui.QColor(color))
            cursor.setCharFormat(char_format)
        
        cursor.insertText(text)
        self.compile_output.setTextCursor(cursor)
        self.compile_output.ensureCursorVisible()
    
    def set_output(self, text):
        """设置编译输出内容"""
        self.compile_output.setPlainText(text)

class CubeSidebar(QtWidgets.QWidget):
    def __init__(self, graph: NodeGraph, properties_widget: PropertiesWidget, compile_widget: CompileWidget, parent=None):
        super().__init__(parent)
        self.graph = graph
        self.properties_widget = properties_widget
        self.compile_widget = compile_widget
        self.setFixedWidth(300)
        self.setup_ui()
        
    def setup_ui(self):
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # 创建选项卡
        self.tab_widget = QtWidgets.QTabWidget()
        self.tab_widget.setTabPosition(QtWidgets.QTabWidget.North)
        
        # 创建属性栏和编译内容栏
        # self.properties_widget = PropertiesWidget()
        # self.compile_widget = CompileWidget()

        # 添加到选项卡
        self.tab_widget.addTab(self.properties_widget, "属性")
        self.tab_widget.addTab(self.compile_widget, "编译")
        
        layout.addWidget(self.tab_widget)
        
    def get_properties_widget(self):
        """获取属性栏组件"""
        return self.properties_widget
    
    def get_compile_widget(self):
        """获取编译内容栏组件"""
        return self.compile_widget
    
    def switch_to_properties(self):
        """切换到属性栏"""
        self.tab_widget.setCurrentIndex(0)
        
    def switch_to_compile(self):
        """切换到编译内容栏"""
        self.tab_widget.setCurrentIndex(1)