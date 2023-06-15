import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QDialog, QVBoxLayout, QLabel
from PyQt5.QtCore import QThread, pyqtSignal, Qt
import requests
from bs4 import BeautifulSoup

class CrawlerThread(QThread):
    crawler_finished = pyqtSignal(list)

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        titles = []
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(self.url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            items = soup.select(".c-single-text-ellipsis")
            for i, item in enumerate(items, start=1):
                title = item.get_text(strip=True)
                titles.append(f"{i}. {title}")
        self.crawler_finished.emit(titles)

class ContentDialog(QDialog):
    def __init__(self, title, url):
        super().__init__()
        self.setWindowTitle(title)
        self.resize(800, 800)
        layout = QVBoxLayout(self)
        self.label = QLabel(self)
        layout.addWidget(self.label)

        self.crawler_thread = CrawlerThread(url)
        self.crawler_thread.crawler_finished.connect(self.update_content)

        self.crawler_thread.start()

    def update_content(self, titles):
        self.label.setText("\n".join(titles))
        self.label.setStyleSheet("font-size: 22px; font-family: Microsoft YaHei;")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("爬虫窗口")
        self.resize(800, 800)
        self.list_widget = QListWidget(self)
        self.setCentralWidget(self.list_widget)

        self.crawler_thread = CrawlerThread("https://top.baidu.com/board?tab=realtime")
        self.crawler_thread.crawler_finished.connect(self.update_list)

        self.crawler_thread.start()

        self.list_widget.itemDoubleClicked.connect(self.open_content_dialog)
        self.list_widget.setStyleSheet("font-size: 22px; font-family: Microsoft YaHei;")

    def update_list(self, titles):
        self.list_widget.addItems(titles)

    def open_content_dialog(self, item):
        title = item.text()
        url = "https://top.baidu.com/board?tab=realtime"  # 在这里设置你要爬取内容的网址
        dialog = ContentDialog(title, url)
        dialog.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
