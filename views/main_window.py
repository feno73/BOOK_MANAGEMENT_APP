# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class ListBookForm(object):
    def setupUi(self, ListBookForm):
        if not ListBookForm.objectName():
            ListBookForm.setObjectName(u"ListBookForm")
        ListBookForm.resize(961, 550)
        self.ButtonsFrame = QFrame(ListBookForm)
        self.ButtonsFrame.setObjectName(u"ButtonsFrame")
        self.ButtonsFrame.setGeometry(QRect(10, 10, 941, 91))
        self.ButtonsFrame.setFrameShape(QFrame.StyledPanel)
        self.ButtonsFrame.setFrameShadow(QFrame.Raised)
        self.openBookButton = QPushButton(self.ButtonsFrame)
        self.openBookButton.setObjectName(u"openBookButton")
        self.openBookButton.setGeometry(QRect(20, 10, 71, 51))
        self.newBookButton = QPushButton(self.ButtonsFrame)
        self.newBookButton.setObjectName(u"newBookButton")
        self.newBookButton.setGeometry(QRect(110, 10, 71, 51))
        self.editBookButton = QPushButton(self.ButtonsFrame)
        self.editBookButton.setObjectName(u"editBookButton")
        self.editBookButton.setGeometry(QRect(200, 10, 71, 51))
        self.deleteBookButton = QPushButton(self.ButtonsFrame)
        self.deleteBookButton.setObjectName(u"deleteBookButton")
        self.deleteBookButton.setGeometry(QRect(290, 10, 71, 51))
        self.frame = QFrame(ListBookForm)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 110, 941, 41))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 71, 16))
        self.searchByComboBox = QComboBox(self.frame)
        self.searchByComboBox.setObjectName(u"searchByComboBox")
        self.searchByComboBox.setGeometry(QRect(70, 10, 161, 22))
        self.parameterLineEdit = QLineEdit(self.frame)
        self.parameterLineEdit.setObjectName(u"parameterLineEdit")
        self.parameterLineEdit.setGeometry(QRect(240, 10, 411, 20))
        self.searchButton = QPushButton(self.frame)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setGeometry(QRect(660, 10, 141, 25))
        self.refreshButton = QPushButton(self.frame)
        self.refreshButton.setObjectName(u"refreshButton")
        self.refreshButton.setGeometry(QRect(800, 10, 141, 25))
        self.listBooksTable = QTableWidget(ListBookForm)
        self.listBooksTable.setObjectName(u"listBooksTable")
        self.listBooksTable.setGeometry(QRect(10, 160, 941, 341))
        self.label_2 = QLabel(ListBookForm)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 520, 111, 16))
        self.booksQtyLabel = QLabel(ListBookForm)
        self.booksQtyLabel.setObjectName(u"booksQtyLabel")
        self.booksQtyLabel.setGeometry(QRect(130, 520, 47, 13))

        self.retranslateUi(ListBookForm)

        QMetaObject.connectSlotsByName(ListBookForm)
    # setupUi

    def retranslateUi(self, ListBookForm):
        ListBookForm.setWindowTitle(QCoreApplication.translate("ListBookForm", u"Books List", None))
        self.openBookButton.setText(QCoreApplication.translate("ListBookForm", u"Abrir Libro", None))
        self.newBookButton.setText(QCoreApplication.translate("ListBookForm", u"Agregar Libro", None))
        self.editBookButton.setText(QCoreApplication.translate("ListBookForm", u"Editar Libro", None))
        self.deleteBookButton.setText(QCoreApplication.translate("ListBookForm", u"Eliminar Libro", None))
        self.label.setText(QCoreApplication.translate("ListBookForm", u"Buscar por:", None))
        self.searchButton.setText(QCoreApplication.translate("ListBookForm", u"Buscar", None))
        self.refreshButton.setText(QCoreApplication.translate("ListBookForm", u"Actualizar", None))
        self.label_2.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p><span style=\" font-weight:600;\">Cantidad de libros:</span></p></body></html>", None))
        self.booksQtyLabel.setText(QCoreApplication.translate("ListBookForm", u"#", None))
    # retranslateUi

