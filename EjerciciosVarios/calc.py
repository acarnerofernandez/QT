import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QVBoxLayout,
    QGridLayout, QPushButton, QWidget, QLineEdit
)


class Fiestra(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora")
        self.setMinimumSize(320, 460)
        self.setMaximumSize(500, 650)

        contenedor = QWidget()
        cajav_principal = QVBoxLayout()
        grid = QGridLayout()
        grid.setSpacing(6)

        self.pantalla_resultado = QLineEdit("")
        self.pantalla_resultado.setReadOnly(True)
        cajav_principal.addWidget(self.pantalla_resultado)

        self.pantalla_operacion = QLineEdit("0")
        self.pantalla_operacion.setReadOnly(True)
        self.pantalla_operacion.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.pantalla_operacion.setFixedHeight(50)
        self.pantalla_operacion.setStyleSheet("font-size: 24px; font-weight: bold;")
        cajav_principal.addWidget(self.pantalla_operacion)

        self.btn_num_0 = QPushButton("0")
        self.btn_num_1 = QPushButton("1")
        self.btn_num_2 = QPushButton("2")
        self.btn_num_3 = QPushButton("3")
        self.btn_num_4 = QPushButton("4")
        self.btn_num_5 = QPushButton("5")
        self.btn_num_6 = QPushButton("6")
        self.btn_num_7 = QPushButton("7")
        self.btn_num_8 = QPushButton("8")
        self.btn_num_9 = QPushButton("9")
        self.btn_coma_decimal = QPushButton(",")

        self.btn_simbolo_borrar = QPushButton("⌦")
        self.btn_simbolo_p_abre = QPushButton("(")
        self.btn_simbolo_p_cierra = QPushButton(")")
        self.btn_simbolo_porcentaje = QPushButton("%")
        self.btn_simbolo_modulo = QPushButton("mod")
        self.btn_simbolo_division = QPushButton("/")
        self.btn_simbolo_multiplicacion = QPushButton("x")
        self.btn_simbolo_resta = QPushButton("-")
        self.btn_simbolo_suma = QPushButton("+")
        self.btn_simbolo_pi = QPushButton("π")
        self.btn_simbolo_raiz = QPushButton("√")
        self.btn_simbolo_cuadrado = QPushButton("x²")
        self.btn_simbolo_signo = QPushButton("±")
        self.btn_simbolo_igual = QPushButton("=")

        self.btn_simbolo_igual.setObjectName("btn_igual")

        botones_numericos = [
            self.btn_num_0, self.btn_num_1, self.btn_num_2, self.btn_num_3,
            self.btn_num_4, self.btn_num_5, self.btn_num_6, self.btn_num_7,
            self.btn_num_8, self.btn_num_9, self.btn_coma_decimal
        ]

        for btn in botones_numericos:
            btn.clicked.connect(self.click_btn_num)


        simbolos = [
            self.btn_simbolo_borrar, self.btn_simbolo_cuadrado, self.btn_simbolo_division, self.btn_simbolo_igual,
            self.btn_simbolo_modulo, self.btn_simbolo_multiplicacion,self.btn_simbolo_p_abre, self.btn_simbolo_p_cierra,
            self.btn_simbolo_pi, self.btn_simbolo_porcentaje, self.btn_simbolo_raiz,self.btn_simbolo_resta, self.btn_simbolo_signo,
            self.btn_simbolo_suma
        ]

        for btn in simbolos:
            btn.clicked.connect(self.click_btn_simbolo)

        columnas = [
            [self.btn_simbolo_borrar, self.btn_num_7, self.btn_num_4, self.btn_num_1, self.btn_num_0],
            [self.btn_simbolo_p_abre, self.btn_num_8, self.btn_num_5, self.btn_num_2, self.btn_coma_decimal],
            [self.btn_simbolo_p_cierra, self.btn_num_9, self.btn_num_6, self.btn_num_3, self.btn_simbolo_porcentaje],
            [self.btn_simbolo_modulo, self.btn_simbolo_division, self.btn_simbolo_multiplicacion, self.btn_simbolo_resta, self.btn_simbolo_suma],
            [self.btn_simbolo_pi, self.btn_simbolo_raiz, self.btn_simbolo_cuadrado, self.btn_simbolo_signo, self.btn_simbolo_igual]
        ]

        for num_col, columna in enumerate(columnas):
            for num_fila, boton in enumerate(columna):
                grid.addWidget(boton, num_fila, num_col)

        cajav_principal.addLayout(grid)
        contenedor.setLayout(cajav_principal)
        self.setCentralWidget(contenedor)

        self.show()

    def click_btn_num(self):
        boton = self.sender()
        numero = boton.text()


        if self.pantalla_operacion.text() == "0" and numero != ",":


            self.pantalla_operacion.setText(numero)
        else:
            self.pantalla_operacion.setText(self.pantalla_operacion.text() + numero)

    def click_btn_simbolo(self):
        boton = self.sender()
        simbolo = boton.text()
        self.pantalla_operacion.setText(self.pantalla_operacion.text() + simbolo)


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = Fiestra()
    aplicacion.exec()