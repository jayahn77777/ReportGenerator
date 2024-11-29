from PyQt5.QtWidgets import QApplication
from ui import TextProcessorApp
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = TextProcessorApp()
    main_window.show()
    sys.exit(app.exec_())
