import io
import sys
import requests

from PyQt6 import uic
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtWidgets import QApplication, QMainWindow
from requests.adapters import HTTPAdapter
from urllib3 import Retry

import ui


static_api = '06100bea-8536-4d5d-916b-a346bb43969e'
spn = '0.002,0.002'

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.session = requests.Session()
        retry = Retry(total=20, connect=10, backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=retry)
        self.session.mount('http://', adapter)
        self.session.mount('https://', adapter)

        f = io.StringIO(ui.MainWindow)
        uic.loadUi(f, self)
        self.findButton.clicked.connect(self.search)

    def search(self):
        ll = self.findEdit.text()
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
