from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Qt
from views.edit_book_window import EditBookForm

class EditBookWindow(QWidget, EditBookForm):
    
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)
        self.setWindowFlag(Qt.Window)

    def populate_inputs(self):
        pass

    def select_file(self):
        pass

    def check_inputs(self):
        pass

    def edit_book(self):
        pass
    
