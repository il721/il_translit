from PyQt6.QtWidgets import QApplication, QWidget

# import sys # Только для доступа к аргументам командной строки

# Приложению нужен один (и только один) экземпляр QApplication.
# Передаём sys.argv, чтобы разрешить аргументы командной строки для приложения.
# Если не будете использовать аргументы командной строки, QApplication([]) тоже работает
app = QApplication([])

# Создаём виджет Qt — окно.
window = QWidget()
window.show()  # Важно: окно по умолчанию скрыто.

app.exec()
