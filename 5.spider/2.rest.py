from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QListWidget, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class WebPageParser:
    def __init__(self):
        self.app = QApplication([])
        self.window = QMainWindow()
        self.webview = QWebEngineView(self.window)
        self.listwidget = QListWidget()
        self.layout = QVBoxLayout()
        self.widget = QWidget()

        self.setup_ui()

    def setup_ui(self):
        self.window.setWindowTitle("Web Page Parser")
        self.layout.addWidget(self.webview)
        self.layout.addWidget(self.listwidget)
        self.widget.setLayout(self.layout)
        self.window.setCentralWidget(self.widget)

    def load_page(self, url):
        self.webview.load(QUrl(url))
        self.webview.loadFinished.connect(self.parse_page)

    def parse_page(self):
        # Extract the data from the loaded web page
        document = self.webview.page().documentElement()
        title_elements = document.findAll("h2.title")
        for title_element in title_elements:
            title_text = title_element.toPlainText()
            list_item = QListWidgetItem(title_text)
            self.listwidget.addItem(list_item)

        self.window.show()
        self.app.exec_()

if __name__ == "__main__":
    parser = WebPageParser()
    parser.load_page("https://blog.misaka.rest/")
