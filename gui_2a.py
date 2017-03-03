import sys
from PyQt5.QtWidgets import (QApplication, QCheckBox, QColorDialog, QDialog,
        QErrorMessage, QFileDialog, QFontDialog, QFrame, QGridLayout,
        QInputDialog, QLabel, QLineEdit, QMessageBox, QPushButton)


def defin_right(d_x):
    d_x_s = str(d_x)
    pos = d_x_s.find('.')
    right = d_x_s[pos + 1:]
    return len(right)


def defin_left(d_x):
    d_x_s = str(d_x)
    pos = d_x_s.find('.')
    left = d_x_s[:pos]
    return len(left)

def defin_delta(delta, d_x):
    if delta == int(delta):
        return 0.5
    leng = defin_right(d_x)
    delta = 5.0 / (10 ** leng)
    for i in range(leng):
        if d_x < delta:
            res_d = delta
            break
        delta *= 10
    return res_d

def len_for_cifr(x):
    return (len(str(x)) - 1)

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

        self.setWindowTitle("2a")

    def setText(self):
        text, ok = QInputDialog.getText(self, "Finding...",
                "Enter your number", QLineEdit.Normal, "NULL")
        if ok and text != '':
            ls = text.split()
            num1 = float(ls[0])
            num2 = float(ls[1])
            print(num1)
            print(num2)
            X = num1 # 72.353
            d_xm = num2 # 0.026
            X_a = X

            delta = defin_delta(d_xm, d_xm)

            if len_for_cifr(X) != len_for_cifr(delta):
                for i in range(len_for_cifr(delta)):
                    X = round(X_a, len_for_cifr(delta) - defin_left(X))
                    dx_abs = d_xm + abs(X_a - X)
                    if dx_abs < delta:
                        break
                    X = round(X_a, len_for_cifr(delta) - defin_left(X) - 1)
                    delta = defin_delta(X, X)
            GLOB = str(X)

            self.textLabel.setText(GLOB)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Dialog()
    dialog.show()
    sys.exit(app.exec_())