from PySide2 import QtCore, QtWidgets, QtGui

from bibindices import Indices

class VerseSelectWidget(QtWidgets.QTabWidget):
    def __init__(self):
        super().__init__()
        self.indices = Indices()
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setAlignment(QtCore.Qt.AlignTop)

        self.book_select_layout = QtWidgets.QHBoxLayout()      
        self.book_select_layout.setAlignment(QtCore.Qt.AlignTop)
        self.book_select_layout.addWidget(QtWidgets.QLabel("Book:"))
        self.book_select = QtWidgets.QComboBox()
        self.book_select.addItems(self.indices.get_books())
        self.book_select_layout.addWidget(self.book_select)
        self.layout.addItem(self.book_select_layout)

        self.chapter_select_layout = QtWidgets.QHBoxLayout()
        self.chapter_select_layout.setAlignment(QtCore.Qt.AlignTop)
        self.chapter_select_layout.addWidget(QtWidgets.QLabel("Chapter:"))
        book = self.book_select.currentText()
        self.chapter_select = QtWidgets.QComboBox()
        self.chapter_select.addItems([str(x) for x in self.indices.get_chapters(book)])
        self.chapter_select_layout.addWidget(self.chapter_select)
        self.layout.addItem(self.chapter_select_layout)

        

        self.setLayout(self.layout)