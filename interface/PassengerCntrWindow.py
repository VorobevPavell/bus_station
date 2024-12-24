"""
Окно подсчета общего количества пассажиров
"""


from PyQt6.QtGui import QWindow
from PyQt6.QtWidgets import QWidget

from core.helpers import Helpers
from database.connection import DatabaseConnection
from dev.passengers import Ui_Passenger


class PassengerCntrWindow(QWidget, Ui_Passenger, QWindow):
    session = DatabaseConnection.get_session()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.helper = Helpers(session=self.session)
        self.passengerCounter.setText(str(self.helper.calculate_passengers()))
        self.backBtn.clicked.connect(self.close)
