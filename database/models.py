"""
Файл содержит в себе классы, которые образуют модели(таблицы) базы данных
"""


from sqlalchemy import Integer, Column, String, ForeignKey, DateTime
from sqlalchemy.orm import DeclarativeBase

from database.connection import DatabaseConnection


class Base(DeclarativeBase):
    pass


class Station(Base):
    """
    Таблица `станция` - Станции, на которые могут прибывать автобусы.
    id: Уникальный номер станции
    name: Название станции
    """

    __tablename__ = "station"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)


class Bus(Base):
    """
    Таблица `автобус` - Автобусы, которые выполняют рейсы до станций.
    id: Уникальный номер автобуса
    brand: Марка автобуса
    state_number: Государственный номер автобуса.
    capacity: Вместительность(чел) автобуса.
    """

    __tablename__ = "bus"

    id = Column(Integer, primary_key=True, autoincrement=True)
    brand = Column(String, nullable=False, unique=True)
    state_number = Column(String, nullable=False, unique=True)
    capacity = Column(Integer, nullable=False, unique=True)


class Route(Base):
    """
    Таблица `рейс` - Рейсы, которые существуют на автовокзале.
    id: Уникальный номер рейса
    station_id: Код станции, на которую прибывает автобус
    bus_id: Код автобуса, который выполняет рейс.
    dep_time: Время отправления автобуса.
    """

    __tablename__ = "route"

    id = Column(Integer, primary_key=True, autoincrement=True)
    station_id = Column(Integer, ForeignKey("station.id"), nullable=False, index=True)
    bus_id = Column(Integer, ForeignKey("bus.id"), nullable=False, index=True)
    dep_time = Column(DateTime, nullable=False)


engine = DatabaseConnection().get_engine()
Base.metadata.create_all(bind=engine)
