"""
Окно удаления рейсов
"""


from venv import logger
from typing import List
from PyQt6.QtGui import QWindow
from PyQt6.QtWidgets import QWidget

from core.routehelper import RouteHelper
from database.connection import DatabaseConnection
from database.models import Route
from dev.del_route import Ui_DelRoute


class DelRoutesWindow(QWidget, Ui_DelRoute, QWindow):
    session = DatabaseConnection.get_session()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.comboBox.addItems(self.get_routes_from_db())
        self.delRouteBtn.clicked.connect(self.del_route_from_db)
        self.backBtn.clicked.connect(self.close)

    def del_route_from_db(self):
        """
        Метод удаляет существующий рейс из базы данных.
        """
        route = self.comboBox.currentText()
        session = DatabaseConnection.get_session()
        db = session()
        route_to_delete = db.query(Route).filter(Route.id == route).scalar()
        if not route_to_delete:
            logger.error("there is no route with %s id", route)
            return
        db.delete(route_to_delete)
        db.commit()
        db.close()
        logger.debug("route deleted from database. id: %s", route)

    def get_routes_from_db(self) -> List[str]:
        """
        Получает все рейсы из базы данных
        """
        route_helpers = RouteHelper(self.session)
        routes = route_helpers.get_all_routes()
        return routes
