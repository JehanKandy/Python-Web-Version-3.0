from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from browserUi import Ui_Form
import sys

# move Window


class movewin(QtWidgets.QWidget):
    def __init__(self):
        super(movewin, self).__init__()

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()


class browserApp(movewin, Ui_Form):
    def __init__(self):
        super(browserApp, self).__init__()
        self.setupUi(self)

        # resize the browser
        self.pushButton.clicked.connect(self.showMinimized)
        self.pushButton_3.clicked.connect(self.winshowMaximized)
        self.pushButton_2.clicked.connect(sys.exit)
        self.lineEdit.returnPressed.connect(self.webload)

        # backward
        self.pushButton_4.clicked.connect(self.backward)
        # forward
        self.pushButton_5.clicked.connect(self.forward)
        # reload
        self.pushButton_6.clicked.connect(self.reload)

   # web load using Url

    def webload(self):
        url = QtCore.QUrl.fromUserInput(self.lineEdit.text())
        if url.isValid():
            self.webEngineView.load(url)

    # for backward
    def backward(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Back)

    # for forward
    def forward(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Forward)

    # for reload
    def reload(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Reload)

    # code for maximized and normal window

    def winshowMaximized(self):
        if self.pushButton_3.isChecked():
            self.showMaximized()
        else:
            self.showNormal()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = browserApp()
    Form.show()
    sys.exit(app.exec())
