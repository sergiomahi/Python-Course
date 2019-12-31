#/usr/bin/python3

import os, sys
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlComponent, QQmlApplicationEngine

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)

    engine = QQmlApplicationEngine()
    engine.load(QUrl.fromLocalFile("main.qml")) # Load a QML file.

    window = engine.rootObjects()[0]
    window.show()

    sys.exit(app.exec_())