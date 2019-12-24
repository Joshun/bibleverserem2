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
        self.book_select.currentTextChanged.connect(self.book_changed)
        self.layout.addItem(self.book_select_layout)

        self.chapter_select_layout = QtWidgets.QHBoxLayout()
        self.chapter_select_layout.setAlignment(QtCore.Qt.AlignTop)
        self.chapter_select_layout.addWidget(QtWidgets.QLabel("Chapter:"))
        book = self.book_select.currentText()
        self.chapter_select = QtWidgets.QComboBox()
        self.chapter_select.addItems([str(x) for x in self.indices.get_chapters(book)])
        self.chapter_select_layout.addWidget(self.chapter_select)
        self.chapter_select.currentTextChanged.connect(self.chapter_changed)
        self.layout.addItem(self.chapter_select_layout)

        self.verse_select_layout = QtWidgets.QHBoxLayout()
        self.verse_select_layout.setAlignment(QtCore.Qt.AlignTop)
        self.verse_select_layout.addWidget(QtWidgets.QLabel("Verse:"))
        chapter = self.chapter_select.currentText()
        self.verse_select = QtWidgets.QComboBox()
        self.verse_select.addItems([str(x) for x in self.indices.get_verses(book, int(chapter))])
        self.verse_select_layout.addWidget(self.verse_select)
        self.layout.addItem(self.verse_select_layout)

        self.setLayout(self.layout)

    def book_changed(self, e):
        self.repopulate_chapter_select()
        self.repopulate_verse_select()

    def chapter_changed(self, e):
        self.repopulate_verse_select()
        
    def repopulate_verse_select(self):
        print("repopuplate verse")
        book = self.book_select.currentText()
        self.verse_select.clear()
        self.verse_select.addItems([str(x) for x in self.indices.get_verses(book, 1)])
        self.verse_select.setCurrentIndex(0)


    def repopulate_chapter_select(self):
        print("repopuplate chapter")
        book = self.book_select.currentText()
        self.chapter_select.clear()
        self.chapter_select.addItems([str(x) for x in self.indices.get_chapters(book)])
        self.chapter_select.setCurrentIndex(0)



