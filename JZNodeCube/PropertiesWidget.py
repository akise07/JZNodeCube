from Qt import QtCore, QtWidgets, QtGui # type: ignore

class PropertiesWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedWidth(300)
        self.setup_ui()
        
    def setup_ui(self):
        layout = QtWidgets.QVBoxLayout(self)
        
        # 添加标题
        title = QtWidgets.QLabel("节点属性")
        title.setStyleSheet("font-weight: bold; font-size: 14px; padding: 5px;")
        layout.addWidget(title)
        
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
        checkbox1.stateChanged.connect(self.on_enable_feature_changed)
        checkbox2.stateChanged.connect(self.on_auto_save_changed)
        checkbox3.stateChanged.connect(self.on_show_grid_changed)
        checkbox4.stateChanged.connect(self.on_enable_animation_changed)
        checkbox5.stateChanged.connect(self.on_debug_mode_changed)
    
    def on_enable_feature_changed(self, state):
        # 处理启用功能状态变化
        print(f"启用功能: {bool(state)}")
    
    def on_auto_save_changed(self, state):
        # 处理自动保存状态变化
        print(f"自动保存: {bool(state)}")
    
    def on_show_grid_changed(self, state):
        # 处理显示网格状态变化
        print(f"显示网格: {bool(state)}")
    
    def on_enable_animation_changed(self, state):
        # 处理启用动画状态变化
        print(f"启用动画: {bool(state)}")
    
    def on_debug_mode_changed(self, state):
        # 处理调试模式状态变化
        print(f"调试模式: {bool(state)}")