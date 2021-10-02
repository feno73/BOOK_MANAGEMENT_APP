from PySide2.QtWidgets import QApplication
from controllers.main_window import ListBookWindow

if __name__ == '__main__':
    app = QApplication()
    window = ListBookWindow()
    window.show()

    app.exec_()


##Link del tutorial: https://www.youtube.com/watch?v=lfMY9FDd_4Q&ab_channel=StraightCoding