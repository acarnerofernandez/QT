import sys
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget, QLabel, QLineEdit)



class FiestraPrincipal (QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mi aplicacion Qt")
        self.setMinimumSize(100,100)
        self.setMaximumSize(2000,2000)
        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.Window, QColor("aquaMarine"))
        self.setPalette(paleta)

        caixaV = QVBoxLayout()


        self.boton = QPushButton("Puslador")
        self.etiqueta = QLabel ( "Ola a todos ")
        self.cadroTexto = QLineEdit()
        self.cadroTexto.setPlaceholderText("Introduce o teu nome")

        self.etiqueta.setText("Otro texto")
        self.cadroTexto.setText("TAmen o podo modificar con outro texto")
        print(self.etiqueta.text())
        print(self.cadroTexto.text())

        self.boton.clicked.connect(self.saudar)
        self.cadroTexto.returnPressed.connect(self.saudar)

        caixaV.addWidget(self.etiqueta)
        caixaV.addWidget(self.cadroTexto)
        caixaV.addWidget(self.boton)

        contedor = QWidget()
        contedor.setLayout(caixaV)
        self.setCentralWidget(contedor)

        self.show()

    def saudar(self):

        usuario = self.cadroTexto.text()

        if len(usuario) != 0:
            self.etiqueta.setText("hola " + usuario)
        else:
            self.etiqueta.setText("porfavor escriba algo")



if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    aplicacion.exec()
