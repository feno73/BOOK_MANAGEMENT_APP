from PySide2.QtWidgets import QWidget, QTableWidgetItem
from views.main_window import ListBookForm
from db.books import select_all_books

class ListBookWindow(QWidget, ListBookForm):

    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.newBookButton.clicked.connect(self.open_new_book_window)
        self.editBookButton.clicked.connect(self.open_edit_book_window)
        self.table_config()
        self.populate_table(select_all_books())

    def open_new_book_window(self):
        from controllers.new_book_window import NewBookWindow
        window = NewBookWindow(self)
        window.show()

    def open_edit_book_window(self):
        from controllers.edit_book_window import EditBookWindow
        window = EditBookWindow(self)
        window.show()

    def open_book(self):
        pass

    def remove_book(self):
        pass

    def table_config(self):
        comlumn_headers = ("ID", "Titulo", "Categoria", "Cantidad de paginas", "Cantidad de paginas leidas", "Ruta", "Descripcion")
        self.listBooksTable.setColumnCount(len(comlumn_headers))
        self.listBooksTable.setHorizontalHeaderLabels(comlumn_headers)

    def populate_table(self, data):
        self.listBooksTable.setRowCount(len(data))
        
        for (index_row, row) in enumerate(data):
            for (index_cell, cell) in enumerate(row):
                self.listBooksTable.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))

    def populate_combobox(self):
        pass

    def search_book_by_title(self):
        pass

    def search_book_by_category(self):
        pass

    def serach(self):
        pass

    def records_qty(self):
        pass