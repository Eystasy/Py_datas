import sys
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QFileDialog, QListWidget, QSlider, QLabel, QSizePolicy
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene

class GraphicsView(QGraphicsView):
    def __init__(self, parent=None):
        super(GraphicsView, self).__init__(parent)
        self.setDragMode(QGraphicsView.ScrollHandDrag)
        self.setRenderHint(QPainter.Antialiasing)
        self.setSceneRect(-500, -500, 1000, 1000)
        self.setRenderHint(QPainter.HighQualityAntialiasing)
        self.setRenderHint(QPainter.SmoothPixmapTransform)

    def wheelEvent(self, event):
        zoomInFactor = 1.25
        zoomOutFactor = 1 / zoomInFactor

        if event.angleDelta().y() > 0:
            zoomFactor = zoomInFactor
        else:
            zoomFactor = zoomOutFactor

        self.scale(zoomFactor, zoomFactor)

class MusicPlayer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Music Player")
        self.setGeometry(200, 200, 500, 500)

        # 创建播放器对象
        self.player = QMediaPlayer()
        self.player.positionChanged.connect(self.update_position)
        self.player.durationChanged.connect(self.update_duration)

        # 创建音乐列表对象
        self.playlist = QMediaPlaylist()
        self.playlist.currentIndexChanged.connect(self.update_current_index)
        self.playlist.setPlaybackMode(QMediaPlaylist.PlaybackMode.Loop)

        # 创建音乐列表视图
        self.music_list = QListWidget()
        self.music_list.doubleClicked.connect(self.play_selected_music)

        # 创建按钮：选择文件、播放、停止、上一曲、下一曲、单曲循环、列表循环
        self.open_button = QPushButton("选择文件")
        self.open_button.clicked.connect(self.open_files)

        self.play_button = QPushButton("播放")
        self.play_button.clicked.connect(self.play_music)

        self.stop_button = QPushButton("停止")
        self.stop_button.clicked.connect(self.stop_music)

        self.previous_button = QPushButton("上一曲")
        self.previous_button.clicked.connect(self.play_previous_music)

        self.next_button = QPushButton("下一曲")
        self.next_button.clicked.connect(self.play_next_music)

        self.single_loop_button = QPushButton("单曲循环")
        self.single_loop_button.setCheckable(True)
        self.single_loop_button.clicked.connect(self.toggle_single_loop)

        self.list_loop_button = QPushButton("列表循环")
        self.list_loop_button.setCheckable(True)
        self.list_loop_button.setChecked(True)
        self.list_loop_button.clicked.connect(self.toggle_list_loop)

        # 创建音乐播放进度滑块和标签
        self.position_slider = QSlider(Qt.Horizontal)
        self.position_slider.setRange(0, 0)
        self.position_slider.sliderMoved.connect(self.set_position)

        self.position_label = QLabel("00:00 / 00:00")

        # 创建音量滑块和标签
        self.volume_slider = QSlider(Qt.Horizontal)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setValue(50)
        self.volume_slider.valueChanged.connect(self.set_volume)

        self.volume_label = QLabel("50%")

        # 创建布局
        layout = QVBoxLayout()
        layout.addWidget(self.music_list)
        layout.addWidget(self.open_button)
        layout.addWidget(self.play_button)
        layout.addWidget(self.stop_button)
        layout.addWidget(self.previous_button)
        layout.addWidget(self.next_button)
        layout.addWidget(self.single_loop_button)
        layout.addWidget(self.list_loop_button)
        layout.addWidget(self.position_slider)
        layout.addWidget(self.position_label)
        layout.addWidget(self.volume_slider)
        layout.addWidget(self.volume_label)

        # 创建主窗口
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def open_files(self):
        # 打开文件选择对话框并选择音乐文件
        files, _ = QFileDialog.getOpenFileNames(self, "选择音乐文件", "", "音乐文件 (*.mp3 *.wav)")

        if files:
            # 将选择的音乐文件添加到音乐列表
            for file in files:
                self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile(file)))
                self.music_list.addItem(file)

            if not self.player.state() == QMediaPlayer.PlayingState:
                # 如果播放器当前未播放音乐，则自动开始播放第一首音乐
                self.player.setPlaylist(self.playlist)
                self.player.play()

    def play_music(self):
        # 播放音乐
        if self.playlist.mediaCount() > 0:
            self.player.setPlaylist(self.playlist)
            self.player.play()

    def stop_music(self):
        # 停止播放音乐
        self.player.stop()

    def play_previous_music(self):
        # 播放上一首音乐
        self.playlist.previous()

    def play_next_music(self):
        # 播放下一首音乐
        self.playlist.next()

    def toggle_single_loop(self):
        # 切换单曲循环模式
        self.playlist.setPlaybackMode(QMediaPlaylist.CurrentItemInLoop if self.single_loop_button.isChecked() else QMediaPlaylist.Loop)

    def toggle_list_loop(self):
        # 切换列表循环模式
        self.playlist.setPlaybackMode(QMediaPlaylist.Loop if self.list_loop_button.isChecked() else QMediaPlaylist.Sequential)

    def update_position(self, position):
        # 更新音乐播放进度
        self.position_slider.setValue(position)

        # 更新音乐播放进度标签
        duration = self.player.duration()
        formatted_position = self.format_time(position)
        formatted_duration = self.format_time(duration)
        self.position_label.setText(f"{formatted_position} / {formatted_duration}")

    def update_duration(self, duration):
        # 更新音乐播放进度条的最大值
        self.position_slider.setRange(0, duration)

    def update_current_index(self, index):
        # 更新音乐列表当前选中项
        self.music_list.setCurrentRow(index)

    def play_selected_music(self, item):
        # 播放所选的音乐
        selected_index = self.music_list.indexFromItem(item).row()
        self.playlist.setCurrentIndex(selected_index)
        self.player.setPlaylist(self.playlist)
        self.player.play()

    def set_position(self, position):
        # 设置音乐播放进度
        self.player.setPosition(position)

    def set_volume(self, volume):
        # 设置音量
        self.player.setVolume(volume)
        self.volume_label.setText(f"{volume}%")

    def format_time(self, milliseconds):
        # 格式化时间（毫秒转为分:秒）
        total_seconds = milliseconds // 1000
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        return f"{minutes:02d}:{seconds:02d}"


if __name__ == "__main__":
    app = QApplication(sys.argv)
    player = MusicPlayer()
    player.show()
    sys.exit(app.exec_())
