import io
import sys
import requests

from PyQt6 import uic
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (QApplication, QDialog, QMainWindow, QFileDialog,
                             QTableWidgetItem, QLabel)
from requests.adapters import HTTPAdapter
from urllib3 import Retry

import ui
static_api = '06100bea-8536-4d5d-916b-a346bb43969e'

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(ui.MainWindow)
        uic.loadUi(f, self)
        self.run()

    def run(self):
        session = requests.Session()
        retry = Retry(total=20, connect=10, backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)

        map_request = f'https://static-maps.yandex.ru/v1?apikey={static_api}'
        response = session.get(map_request)

        if not response:
            print("Ошибка выполнения запроса:")
            print(map_request)
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)
