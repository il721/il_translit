import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_Il_Translit import Ui_MainWindow


class TranslatePySide(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.translit_button.clicked.connect(self.input_text)
        self.ui.clear_button.clicked.connect(self.clear_in_text)

    def input_text(self):
        text_in = self.ui.input_window.text()
        self.ui.output_window.setText(text_in)

    def clear_in_text(self):
        self.ui.input_window.clear()


if __name__ == '__main__':
    app = QApplication([])
    window = TranslatePySide()
    window.show()
    sys.exit(app.exec())
