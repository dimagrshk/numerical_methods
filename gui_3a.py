import sys
import math
from PyQt5.QtCore import QDir, Qt
from PyQt5.QtGui import QFont, QPalette
from PyQt5.QtWidgets import (QApplication, QCheckBox, QColorDialog, QDialog,
        QErrorMessage, QFileDialog, QFontDialog, QFrame, QGridLayout,
        QInputDialog, QLabel, QLineEdit, QMessageBox, QPushButton)

GLOB = 0.0

def defin_right(d_x):
    if d_x ==int(d_x):
        return 0.5
    d_x_s = str(d_x)
    pos = d_x_s.find('.')
    right = d_x_s[pos + 1:]

    return 5.0/(10**(len(right)+1))

def limit(sigma):
    s_sigma = str(sigma)
    pos = s_sigma.find('.')
    right = s_sigma[pos + 1:]
    lis_right = list(right)
    count = 1
    for c in lis_right:
        if c == '0':
            count += 1
    mnog = 10**count
    tmp = sigma * mnog
    tmp = math.ceil(tmp)
    return tmp / mnog


class Dialog(QDialog):
    GLOB = 0.0
    MESSAGE = "dimagrishko"
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)

        self.openFilesPath = ''

        self.errorMessageDialog = QErrorMessage(self)

        frameStyle = QFrame.Sunken | QFrame.Panel
        self.textLabel = QLabel()
        self.textLabel.setFrameStyle(frameStyle)
        self.textButton = QPushButton("Press")



        self.textButton.clicked.connect(self.setText)


        self.native = QCheckBox()
        self.native.setText("Use native file dialog.")
        self.native.setChecked(True)
        if sys.platform not in ("win32", "darwin"):
            self.native.hide()

        layout = QGridLayout()
        layout.setColumnStretch(1, 1)
        layout.setColumnMinimumWidth(1, 250)
        layout.addWidget(self.textButton, 3, 0)
        layout.addWidget(self.textLabel, 3, 1)

        self.setLayout(layout)

        self.setWindowTitle("3a")
    def setText(self):
        text, ok = QInputDialog.getText(self, "Finding...",
                "Enter your number", QLineEdit.Normal, "NULL")
        if ok and text != '':
            ls = text.split()
            num1 = float(ls[0])
            print(num1)
            delta = defin_right(num1)
            s_x = delta/num1
            GLOB = str(limit(s_x))
            print(limit(s_x))
            self.textLabel.setText("limit relative error  = " + GLOB + ", absol error = " + str(delta))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Dialog()
    dialog.show()
    sys.exit(app.exec_())