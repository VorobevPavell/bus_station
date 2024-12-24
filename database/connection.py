"""
Файл для работы с подключением к базе данных sqlite.
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DatabaseConnection:
    """
    Класс отвечает за подключение к базе данных.
    """

    DATABASE_CONNECTION_URL = "sqlite:///demoexamq.db"
    engine = create_engine(DATABASE_CONNECTION_URL)
    session = sessionmaker(bind=engine)

    @classmethod
    def get_session(cls):
        """
        Метод для получения сессии подключения к базе.
        :return: Объект session
        """
        return cls.session

    @classmethod
    def get_engine(cls):
        """
        Метод для получения движка для соединения с базой.
        :return: Объект engine
        """
        return cls.engine
