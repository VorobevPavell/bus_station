"""
Главный файл приложения.
"""

from PyQt6.QtWidgets import QApplication

from interface.MainWindow import MainWindow


def main():
    """
    Функция инициализирует и запускает главное окно приложения.
    """
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
