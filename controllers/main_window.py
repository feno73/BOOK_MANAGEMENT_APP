from PySide2.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView
from views.main_window import ListBookForm
from db.books import select_all_books, select_book_by_title, select_book_by_category, delete_book
import os

class ListBookWindow(QWidget, ListBookForm):

    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.newBookButton.clicked.connect(self.open_new_book_window)
        self.editBookButton.clicked.connect(self.open_edit_book_window)
        self.table_config()
        self.populate_table(select_all_books())
        self.populate_combobox()
        self.refreshButton.clicked.connect(lambda: self.populate_table(select_all_books()))
        self.openBookButton.clicked.connect(self.open_book)
        self.searchButton.clicked.connect(self.search)
        self.deleteBookButton.clicked.connect(self.remove_book)

    def open_new_book_window(self):
        from controllers.new_book_window import NewBookWindow
        window = NewBookWindow(self)
        window.show()

    def open_edit_book_window(self):
        from controllers.edit_book_window import EditBookWindow
        selected_row = self.listBooksTable.selectedItems()

        if selected_row:
            book_id = int(selected_row[0].text())
            window = EditBookWindow(self, book_id)
            window.show()
        
        self.listBooksTable.clearSelection()

        

    def open_book(self):
        selected_row = self.listBooksTable.selectedItems()

        if selected_row:
            path = selected_row[5].text()
            os.startfile(path)
        
        self.listBooksTable.clearSelection()

    def remove_book(self):
        selected_row = self.listBooksTable.selectedItems()

        if selected_row:
            book_id = int(selected_row[0].text())
            row = selected_row[0].row()

            if delete_book(book_id):
                file_path = selected_row[5].text()
                self.listBooksTable.removeRow(row)
                os.remove(file_path)
        
        self.records_qty()




    def table_config(self):
        comlumn_headers = ("ID", "Titulo", "Categoria", "Cantidad de paginas", "Cantidad de paginas leidas", "Ruta", "Descripcion")
        self.listBooksTable.setColumnCount(len(comlumn_headers))
        self.listBooksTable.setHorizontalHeaderLabels(comlumn_headers)

        self.listBooksTable.setSelectionBehavior(QAbstractItemView.SelectRows)

    def populate_table(self, data):
        self.listBooksTable.setRowCount(len(data))
        
        for (index_row, row) in enumerate(data):
            for (index_cell, cell) in enumerate(row):
                self.listBooksTable.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))
        
        self.records_qty()

    def populate_combobox(self):
        cb_options = ("", "Titulo", "Categoria")
        self.searchByComboBox.addItems(cb_options)

    def search_book_by_title(self, title):
        data = select_book_by_title(title)
        self.populate_table(data)

    def search_book_by_category(self, category):
        data = select_book_by_category(category)
        self.populate_table(data)

    def search(self):
        option_selected = self.searchByComboBox.currentText()
        parameter = self.parameterLineEdit.text()

        if option_selected == "":
            print("Debe seleccionar una opcion")
        else:
            if parameter == "":
                print("El campo de busqueda esta vacio")
            else:
                if option_selected == "Titulo":
                    self.search_book_by_title(parameter)
                elif option_selected == "Categoria":
                    self.search_book_by_category(parameter)
        
        

    def records_qty(self):
        qty_rows = str(self.listBooksTable.rowCount())
        self.booksQtyLabel.setText(qty_rows)