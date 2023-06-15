import sys
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QFileDialog, QListWidget
from PyQt6.QtMultimedia import QMediaPlayer
from PyQt6.QtMultimediaWidgets import QVideoWidget

class MusicPlayer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Music Player")
        self.setGeometry(200, 200, 300, 300)

        # 创建播放器对象
        self.player = QMediaPlayer()

        # 创建音乐列表视图
        self.music_list = QListWidget()

        # 创建按钮：选择文件、播放、停止、单曲循环、列表循环
        self.open_button = QPushButton("选择文件")
        self.open_button.clicked.connect(self.open_files)

        self.play_button = QPushButton("播放")
        self.play_button.clicked.connect(self.play_music)

        self.stop_button = QPushButton("停止")
        self.stop_button.clicked.connect(self.stop_music)

        self.single_loop_button = QPushButton("单曲循环")
        self.single_loop_button.setCheckable(True)
        self.single_loop_button.clicked.connect(self.toggle_single_loop)

        self.list_loop_button = QPushButton("列表循环")
        self.list_loop_button.setCheckable(True)
        self.list_loop_button.setChecked(True)
        self.list_loop_button.clicked.connect(self.toggle_list_loop)

        # 创建布局并添加部件
        layout = QVBoxLayout()
        layout.addWidget(self.open_button)
        layout.addWidget(self.play_button)
        layout.addWidget(self.stop_button)
        layout.addWidget(self.single_loop_button)
        layout.addWidget(self.list_loop_button)
        layout.addWidget(self.music_list)

        # 创建主部件并设置布局
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def open_files(self):
        # 打开文件对话框，选择要导入的音乐文件
        files, _ = QFileDialog.getOpenFileUrls(self, "选择音乐文件", "", "音乐文件 (*.mp3 *.wav)")

        if files:
            # 清空音乐列表
            self.music_list.clear()

            # 将选择的音乐文件添加到音乐列表
            for file in files:
                self.music_list.addItem(file.fileName())

                # 创建音乐内容对象
                content = QUrl.fromLocalFile(file.toLocalFile())

                # 将音乐内容设置给播放器
                self.player.setMedia(content)

    def play_music(self):
        # 播放音乐
        self.player.play()

    def stop_music(self):
        # 停止播放音乐
        self.player.stop()

    def toggle_single_loop(self):
        # 切换单曲循环模式
        self.player.setLoopCount(-1 if self.single_loop_button.isChecked() else 0)

    def toggle_list_loop(self):
        # 切换列表循环模式
        self.player.setPlaylist(self.playlist)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    player = MusicPlayer()
    player.show()
    sys.exit(app.exec())
