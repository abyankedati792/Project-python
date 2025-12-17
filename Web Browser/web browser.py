import sys
from PyQt5.QtWidgets import QApplication, QLineEdit, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Python Web Browser")
window.resize(1200, 800)

layout = QVBoxLayout()

url_bar = QLineEdit()
browser = QWebEngineView()
browser.setUrl(QUrl("https://www.google.com"))

def load_url():
    url = url_bar.text()
    if not url.startswith("http"):
        url = "https://" + url
    browser.setUrl(QUrl(url))

url_bar.returnPressed.connect(load_url)

layout.addWidget(url_bar)
layout.addWidget(browser)

window.setLayout(layout)
window.show()

sys.exit(app.exec_())
