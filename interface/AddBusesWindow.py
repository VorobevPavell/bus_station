"""
Окно добавления автобусов
"""


from venv import logger

from PyQt6.QtGui import QWindow
from PyQt6.QtWidgets import QWidget

from database.connection import DatabaseConnection
from database.models import Bus
from dev.add_buses import Ui_Bus


class AddBusesWindow(QWidget, Ui_Bus, QWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.addBusBtn.clicked.connect(self.add_bus_into_db)
        self.backBtn.clicked.connect(self.close)

    def add_bus_into_db(self):
        """
        Метод добавляет новый автобус в базу данных.
        :return:
        """
        brand = self.brand.text()
        cap = self.busCapacity.text()
        state_number = self.stateNumber.text()
        session = DatabaseConnection.get_session()
        db = session()
        if db.query(Bus).filter(Bus.state_number == state_number).scalar():
            logger.error("bus already exists with %s state_number", state_number)
            return
        new_bus = Bus(brand=brand, capacity=cap, state_number=state_number)
        db.add(new_bus)
        db.commit()
        db.close()
        logger.debug(
            "bus added to database. brand: %s capacity: %s state_number: %s",
            brand,
            cap,
            state_number,
        )
