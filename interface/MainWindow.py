"""
Главное окно приложения
"""


from PyQt6.QtWidgets import QMainWindow

from dev.main_window import Ui_MainWindow
from interface.AddBusesWindow import AddBusesWindow
from interface.DelBusesWindow import DelBusesWindow
from interface.CalculateRoutesWindow import CalculateRoutesWindow
from interface.DelStationWindow import DelStationWindow
from interface.DelRouteWindow import DelRoutesWindow
from interface.PassengerCntrWindow import PassengerCntrWindow
from interface.AddStationWindow import AddStationWindow
from interface.AddRouteWindow import AddRouteWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.calcRoutesBtn.clicked.connect(self.to_calculate_routes_window)
        self.passangerCountBtn.clicked.connect(self.to_passenger_counter_window)
        self.addBusBtn.clicked.connect(self.to_add_bus_btn_window)
        self.delBusBtn.clicked.connect(self.to_del_bus_btn_window)
        self.addStationBtn.clicked.connect(self.to_add_station_btn_window)
        self.delStationBtn.clicked.connect(self.to_del_station_btn_window)
        self.addRouteBtn.clicked.connect(self.to_add_route_btn_window)
        self.delRouteBtn.clicked.connect(self.to_del_route_btn_window)

    def to_calculate_routes_window(self):
        self.calculate_window = CalculateRoutesWindow()
        self.calculate_window.show()

    def to_passenger_counter_window(self):
        self.passenger_counter_window = PassengerCntrWindow()
        self.passenger_counter_window.show()

    def to_add_bus_btn_window(self):
        self.add_bus_window = AddBusesWindow()
        self.add_bus_window.show()

    def to_del_bus_btn_window(self):
        self.del_bus_window = DelBusesWindow()
        self.del_bus_window.show()

    def to_add_station_btn_window(self):
        self.add_station_window = AddStationWindow()
        self.add_station_window.show()

    def to_del_station_btn_window(self):
        self.del_station_window = DelStationWindow()
        self.del_station_window.show()

    def to_add_route_btn_window(self):
        self.add_route_window = AddRouteWindow()
        self.add_route_window.show()

    def to_del_route_btn_window(self):
        self.del_route_window = DelRoutesWindow()
        self.del_route_window.show()
