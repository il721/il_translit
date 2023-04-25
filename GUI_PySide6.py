import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_Il_Translit import Ui_MainWindow
from transliterate import translit
import pyperclip as pc


class TranslatePySide(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.translit_button.clicked.connect(self.translit_in_text)
        self.ui.clear_button.clicked.connect(self.clear_in_text)

    def translit_in_text(self) -> None:
        """
        Translit and copy to clipboard input text
        """
        text_in = self.ui.input_window.text()
        text_out = translit(text_in, 'ru')
        pc.copy(text_out)
        self.ui.output_window.setText(text_out)

    def clear_in_text(self) -> None:
        """
        Clear text in input/output window when press button clear
        """
        self.ui.input_window.clear()
        self.ui.output_window.clear()


if __name__ == '__main__':
    app = QApplication([])
    window = TranslatePySide()
    window.show()
    sys.exit(app.exec())
