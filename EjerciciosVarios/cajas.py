import sys
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QLabel, QLineEdit)


class CaixaCor(QWidget):
    def __init__(self,color):
        super().__init__()
        self.setAutoFillBackground(True)
        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(paleta)


class Fiestra (QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cajas")
        self.setMinimumSize(300,200)
        self.setMaximumSize(500,400)

        contenedor = QWidget()
        cajah_principal = QHBoxLayout()
        bloqueizq = QVBoxLayout()
        bloquecent = QVBoxLayout()
        bloqueder = QVBoxLayout()

        bloqueizq.addWidget(CaixaCor("red"))
        bloqueizq.addWidget(CaixaCor("yellow"))
        bloqueizq.addWidget(CaixaCor("purple"))

        bloquecent.addWidget(CaixaCor("green"))

        bloqueder.addWidget(CaixaCor("red"))
        bloqueder.addWidget(CaixaCor("purple"))

        cajah_principal.addLayout(bloqueizq)
        cajah_principal.addLayout(bloquecent)
        cajah_principal.addLayout(bloqueder)


        contenedor.setLayout(cajah_principal)

        self.setCentralWidget(contenedor)

        self.show()


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = Fiestra()
    aplicacion.exec()




