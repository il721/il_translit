import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_Il_Translit import Ui_MainWindow


class TranslatePySide(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication([])
    window = TranslatePySide()
    window.show()
    sys.exit(app.exec())
