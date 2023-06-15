import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QListView
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl

class MusicPlayer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Music Player")
        self.setGeometry(200, 200, 300, 300)

        # 创建播放器对象
        self.player = QMediaPlayer()

        # 创建选择文件按钮
        self.open_button = QPushButton("选择文件")
        self.open_button.clicked.connect(self.open_file)

        # 创建播放按钮
        self.play_button = QPushButton("播放")
        self.play_button.clicked.connect(self.play_music)

        # 创建停止按钮
        self.stop_button = QPushButton("停止")
        self.stop_button.clicked.connect(self.stop_music)

        # 创建音乐列表视图和模型
        self.music_list_view = QListView()
        self.music_model = QStandardItemModel()
        self.music_list_view.setModel(self.music_model)

        # 创建布局，并将按钮和音乐列表视图添加到布局中
        layout = QVBoxLayout()
        layout.addWidget(self.open_button)
        layout.addWidget(self.play_button)
        layout.addWidget(self.stop_button)
        layout.addWidget(self.music_list_view)

        # 创建主部件，并将布局设置为主部件的布局
        widget = QWidget()
        widget.setLayout(layout)

        # 将主部件设置为主窗口的中心部件
        self.setCentralWidget(widget)

    def open_file(self):
        # 打开文件对话框，选择要播放的音乐文件
        file, _ = QFileDialog.getOpenFileName(self, "选择音乐文件", "", "音乐文件 (*.mp3)")

        if file:
            # 创建音乐内容对象
            content = QMediaContent(QUrl.fromLocalFile(file))

            # 设置播放器的内容
            self.player.setMedia(content)

            # 将选择的音乐文件添加到音乐列表视图中
            item = QStandardItem(file)
            self.music_model.appendRow(item)

    def play_music(self):
        # 播放音乐
        self.player.play()

    def stop_music(self):
        # 停止音乐
        self.player.stop()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MusicPlayer()
    window.show()
    sys.exit(app.exec_())
