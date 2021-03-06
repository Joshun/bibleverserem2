import sys
from PySide2 import QtCore, QtWidgets, QtGui

# from pysword.modules import SwordModules
from bibindices import Indices

from verseselectwidget import VerseSelectWidget

class TimeSelectWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QtWidgets.QHBoxLayout()
        self.setLayout(self.layout)
        self.layout.setAlignment(QtCore.Qt.AlignTop)
        self.layout.addWidget(QtWidgets.QLabel("Time delay (minutes):"))
        self.time_select_widget = QtWidgets.QSpinBox()
        self.layout.addWidget(self.time_select_widget)

class VersionSelectWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QtWidgets.QHBoxLayout()
        self.layout.setAlignment(QtCore.Qt.AlignTop)
        self.setLayout(self.layout)
        online_select = QtWidgets.QRadioButton("Online")
        sword_select = QtWidgets.QRadioButton("Sword module")
        self.layout.addWidget(online_select)
        self.layout.addWidget(sword_select)

class MainWindow(QtWidgets.QTabWidget):
    def __init__(self):
        super().__init__()


        self.toplevel_layout = QtWidgets.QVBoxLayout()
        self.toplevel_layout.setAlignment(QtCore.Qt.AlignTop)

        self.version_select = VersionSelectWidget()
        self.addTab(self.version_select, "Version")

        self.verse_select_widget = VerseSelectWidget()
        self.addTab(self.verse_select_widget, "Verse")
        # self.verse_select_widget.show()

        self.time_select_widget = TimeSelectWidget()
        self.addTab(self.time_select_widget, "Time")
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