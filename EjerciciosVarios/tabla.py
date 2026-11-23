import sys
from PyQt6.QtCore import Qt, QAbstractTableModel
from PyQt6.QtGui import QColor  # <--- Importamos QColor
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableView, QVBoxLayout, QWidget


class ModeloTaboa(QAbstractTableModel):
    def __init__(self, datos):
        super().__init__()
        self._datos = datos

    def rowCount(self, index):
        return len(self._datos)

    def columnCount(self, index):
        return len(self._datos[0])

    def data(self, index, role):
        fila = index.row()
        columna = index.column()
        valor = self._datos[fila][columna]

        # 1. Gestión del color de fondo (BackgroundRole)
        if role == Qt.ItemDataRole.BackgroundRole:
            # Ignoramos la fila 0 porque es la cabecera ("Nome", "Dni", etc.)
            if fila > 0:
                xenero = self._datos[fila][2]  # La columna 2 es "Xenero"

                # Si quieres colorear SOLO la celda del género, añade: and columna == 2
                if xenero == "Muller":
                    return QColor("#FFC0CB")  # Rosa claro (Pink)
                elif xenero == "Home":
                    return QColor("#ADD8E6")  # Azul claro (LightBlue)

        # 2. Gestión del checkbox para booleanos
        if isinstance(valor, bool):
            if role == Qt.ItemDataRole.CheckStateRole:
                return Qt.CheckState.Checked if valor else Qt.CheckState.Unchecked
            return None

        # 3. Gestión del texto normal
        if role == Qt.ItemDataRole.DisplayRole:
            return valor

        return None

    def flags(self, index):
        valor = self._datos[index.row()][index.column()]
        if isinstance(valor, bool):
            return Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsSelectable
        return super().flags(index)

    def setData(self, index, value, role):
        if role == Qt.ItemDataRole.CheckStateRole and isinstance(self._datos[index.row()][index.column()], bool):
            self._datos[index.row()][index.column()] = (value == Qt.CheckState.Checked.value)
            self.dataChanged.emit(index, index)
            return True
        return False


class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exemplo QTableView")

        datos = [
            ["Nome", "Dni", "Xenero", "Falecido"],
            ["Ana Perez", "1111R", "Muller", False],
            ["Paco Porras", "2222T", "Home", True],
            ["Roque Vila", "3333H", "Home", False],
        ]

        self.modelo = ModeloTaboa(datos)

        caixaV = QVBoxLayout()

        self.tvwTaboa = QTableView()
        self.tvwTaboa.setModel(self.modelo)

        caixaV.addWidget(self.tvwTaboa)

        contedor = QWidget()
        contedor.setLayout(caixaV)
        self.setCentralWidget(contedor)

        self.show()


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    aplicacion.exec()