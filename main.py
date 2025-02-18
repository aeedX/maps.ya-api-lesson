import io
import sys
import requests

from PyQt6 import uic
from PyQt6 import QtCore
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtWidgets import QApplication, QMainWindow
from requests.adapters import HTTPAdapter
from urllib3 import Retry

import ui


static_api = '06100bea-8536-4d5d-916b-a346bb43969e'

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.session = requests.Session()
        retry = Retry(total=20, connect=10, backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=retry)
        self.session.mount('http://', adapter)
        self.session.mount('https://', adapter)

        self.spn = 0.002

        f = io.StringIO(ui.MainWindow)
        uic.loadUi(f, self)
        self.findButton.clicked.connect(self.search)

    def search(self):
        ll = self.findEdit.text()
        if not ll:
            return
        spn = f'{self.spn},{self.spn}'
        map_request = f'https://static-maps.yandex.ru/v1?apikey={static_api}&ll={ll}&spn={spn}'
        response = self.session.get(map_request)

        if not response:
            print("Ошибка выполнения запроса:")
            print(map_request)
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)

        img = QImage.fromData(response.content)
        pixmap = QPixmap.fromImage(img)
        self.map.setPixmap(pixmap)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key.Key_PageUp and self.spn < 0.1:
            self.spn += 0.001
            self.search()
            print(self.spn)
        elif event.key() == QtCore.Qt.Key.Key_PageDown and self.spn > 0:
            self.spn -= 0.001
            self.search()
            print(self.spn)
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
