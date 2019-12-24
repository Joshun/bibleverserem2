import sys
from PySide2 import QtCore, QtWidgets, QtGui

# from pysword.modules import SwordModules
from bibindices import Indices

from verseselectwidget import VerseSelectWidget

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.toplevel_layout = QtWidgets.QVBoxLayout()

        self.verse_select_widget = VerseSelectWidget()
        self.toplevel_layout.addWidget(self.verse_select_widget)
        self.verse_select_widget.show()
        # self.verse_select_layout = QtWidgets.QHBoxLayout()        
        # self.verse_select_layout.addWidget(QtWidgets.QLabel("Book:"))
        # self.book_select = QtWidgets.QComboBox()

        # self.indices = Indices()
        # self.book_select.addItems(self.indices.get_books())
        
        # self.verse_select_layout.addWidget(self.book_select)


        # self.toplevel_layout.addItem(self.verse_select_layout)
        self.setLayout(self.toplevel_layout)

# class BibleLoader:
#     def __init__(self, filename):
#         self.modules = SwordModules(filename)
#         found_modules = self.modules.parse_modules()
#         print("Loaded", found_modules)




def main():

    app = QtWidgets.QApplication([])

    widget = MainWindow()
    widget.resize(640,480)
    widget.show()

    sys.exit(app.exec_())



if __name__ == "__main__":
    main()