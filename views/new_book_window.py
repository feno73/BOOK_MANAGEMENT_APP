# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_book_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class NewBookForm(object):
    def setupUi(self, newBookWindow):
        if not newBookWindow.objectName():
            newBookWindow.setObjectName(u"newBookWindow")
        newBookWindow.resize(405, 472)
        newBookWindow.setCursor(QCursor(Qt.ArrowCursor))
        self.label = QLabel(newBookWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 381, 20))
        self.label.setFrameShape(QFrame.Box)
        self.label_2 = QLabel(newBookWindow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 60, 61, 13))
        self.titleLineEdit = QLineEdit(newBookWindow)
        self.titleLineEdit.setObjectName(u"titleLineEdit")
        self.titleLineEdit.setGeometry(QRect(30, 80, 351, 20))
        self.label_3 = QLabel(newBookWindow)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 110, 81, 16))
        self.categoryLineEdit = QLineEdit(newBookWindow)
        self.categoryLineEdit.setObjectName(u"categoryLineEdit")
        self.categoryLineEdit.setGeometry(QRect(30, 130, 271, 20))
        self.pageQtySpinBox = QSpinBox(newBookWindow)
        self.pageQtySpinBox.setMaximum(9999)
        self.pageQtySpinBox.setObjectName(u"pageQtySpinBox")
        self.pageQtySpinBox.setGeometry(QRect(30, 180, 101, 22))
        self.label_4 = QLabel(newBookWindow)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 160, 151, 16))
        self.label_5 = QLabel(newBookWindow)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 210, 151, 16))
        self.filePathLineEdit = QLineEdit(newBookWindow)
        self.filePathLineEdit.setObjectName(u"filePathLineEdit")
        self.filePathLineEdit.setGeometry(QRect(30, 230, 191, 20))
        self.selectFileButton = QPushButton(newBookWindow)
        self.selectFileButton.setObjectName(u"selectFileButton")
        self.selectFileButton.setGeometry(QRect(230, 230, 25, 20))
        self.selectFileButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_6 = QLabel(newBookWindow)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 280, 151, 16))
        self.descriptionTextEdit = QTextEdit(newBookWindow)
        self.descriptionTextEdit.setObjectName(u"descriptionTextEdit")
        self.descriptionTextEdit.setGeometry(QRect(30, 300, 351, 111))
        self.addButton = QPushButton(newBookWindow)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(30, 430, 75, 23))
        self.cancelButton = QPushButton(newBookWindow)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(120, 430, 75, 23))
        self.cancelButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.retranslateUi(newBookWindow)

        QMetaObject.connectSlotsByName(newBookWindow)
    # setupUi

    def retranslateUi(self, newBookWindow):
        newBookWindow.setWindowTitle(QCoreApplication.translate("newBookWindow", u"Nuevo Libro", None))
        self.label.setText(QCoreApplication.translate("newBookWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">NUEVO LIBRO</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("newBookWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">TITULO</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("newBookWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">CATEGORIA</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("newBookWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">CANTIDAD DE PAGINAS</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("newBookWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">SELECCIONAR ARCHIVO</span></p></body></html>", None))
        self.selectFileButton.setText(QCoreApplication.translate("newBookWindow", u"...", None))
        self.label_6.setText(QCoreApplication.translate("newBookWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">DESCRIPCION DEL LIBRO</span></p></body></html>", None))
        self.addButton.setText(QCoreApplication.translate("newBookWindow", u"Agregar Libro", None))
        self.cancelButton.setText(QCoreApplication.translate("newBookWindow", u"Cancelar", None))
    # retranslateUi

