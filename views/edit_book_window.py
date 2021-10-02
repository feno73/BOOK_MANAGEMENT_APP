# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_book_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class EditBookForm(object):
    def setupUi(self, editBookWindow):
        if not editBookWindow.objectName():
            editBookWindow.setObjectName(u"editBookWindow")
        editBookWindow.resize(405, 596)
        editBookWindow.setCursor(QCursor(Qt.ArrowCursor))
        self.label = QLabel(editBookWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 381, 20))
        self.label.setFrameShape(QFrame.Box)
        self.label_2 = QLabel(editBookWindow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 60, 61, 13))
        self.titleLineEdit = QLineEdit(editBookWindow)
        self.titleLineEdit.setObjectName(u"titleLineEdit")
        self.titleLineEdit.setGeometry(QRect(30, 80, 351, 20))
        self.label_3 = QLabel(editBookWindow)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 110, 81, 16))
        self.categoryLineEdit = QLineEdit(editBookWindow)
        self.categoryLineEdit.setObjectName(u"categoryLineEdit")
        self.categoryLineEdit.setGeometry(QRect(30, 130, 271, 20))
        self.pageQtySpinBox = QSpinBox(editBookWindow)
        self.pageQtySpinBox.setObjectName(u"pageQtySpinBox")
        self.pageQtySpinBox.setGeometry(QRect(30, 180, 101, 22))
        self.label_4 = QLabel(editBookWindow)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 160, 151, 16))
        self.label_5 = QLabel(editBookWindow)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 320, 151, 16))
        self.filePathLineEdit = QLineEdit(editBookWindow)
        self.filePathLineEdit.setObjectName(u"filePathLineEdit")
        self.filePathLineEdit.setGeometry(QRect(30, 340, 191, 20))
        self.selectFileButton = QPushButton(editBookWindow)
        self.selectFileButton.setObjectName(u"selectFileButton")
        self.selectFileButton.setGeometry(QRect(230, 340, 25, 20))
        self.selectFileButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_6 = QLabel(editBookWindow)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 390, 151, 16))
        self.descriptionTextEdit = QTextEdit(editBookWindow)
        self.descriptionTextEdit.setObjectName(u"descriptionTextEdit")
        self.descriptionTextEdit.setGeometry(QRect(30, 410, 351, 111))
        self.editButton = QPushButton(editBookWindow)
        self.editButton.setObjectName(u"editButton")
        self.editButton.setGeometry(QRect(30, 540, 75, 23))
        self.cancelButton = QPushButton(editBookWindow)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(120, 540, 75, 23))
        self.cancelButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pageReadQtySpinBox = QSpinBox(editBookWindow)
        self.pageReadQtySpinBox.setObjectName(u"pageReadQtySpinBox")
        self.pageReadQtySpinBox.setGeometry(QRect(30, 240, 101, 22))
        self.label_7 = QLabel(editBookWindow)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 220, 151, 16))

        self.retranslateUi(editBookWindow)

        QMetaObject.connectSlotsByName(editBookWindow)
    # setupUi

    def retranslateUi(self, editBookWindow):
        editBookWindow.setWindowTitle(QCoreApplication.translate("editBookWindow", u"Editar Libro", None))
        self.label.setText(QCoreApplication.translate("editBookWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">EDITAR LIBRO</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("editBookWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">TITULO</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("editBookWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">CATEGORIA</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("editBookWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">CANTIDAD DE PAGINAS</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("editBookWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">SELECCIONAR ARCHIVO</span></p></body></html>", None))
        self.selectFileButton.setText(QCoreApplication.translate("editBookWindow", u"...", None))
        self.label_6.setText(QCoreApplication.translate("editBookWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">DESCRIPCION DEL LIBRO</span></p></body></html>", None))
        self.editButton.setText(QCoreApplication.translate("editBookWindow", u"Editar Libro", None))
        self.cancelButton.setText(QCoreApplication.translate("editBookWindow", u"Cancelar", None))
        self.label_7.setText(QCoreApplication.translate("editBookWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">CANTIDAD DE PAGINAS LEIDAS</span></p></body></html>", None))
    # retranslateUi

