"""
Окно расчета маршрутов до станции.
"""


from PyQt6.QtGui import QWindow
from PyQt6.QtWidgets import QWidget

from core.helpers import Helpers
from core.stationhelper import StationHelper
from database.connection import DatabaseConnection
from dev.calculate_routes import Ui_Form


class CalculateRoutesWindow(QWidget, Ui_Form, QWindow):
    session = DatabaseConnection.get_session()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.comboBox.addItems(self.get_stations_from_db())
        self.calcRoutesBtn.clicked.connect(self.show_routes_cnt)
        self.backBtn.clicked.connect(self.close)
        self.helper = Helpers(session=self.session)

    def show_routes_cnt(self):
        routes_cnt = self.helper.calculate_routes_to_station(
            self.comboBox.currentText()
        )
        self.label.setText(str(routes_cnt))

    def get_stations_from_db(self):
        station_base = StationHelper(self.session)
        stations = station_base.get_all_stations()
        return stations
