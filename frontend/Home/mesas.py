from PyQt5 import QtWidgets, QtCore

class MesasWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BaristaPost - Gestión de Mesas")
        self.setGeometry(200, 200, 500, 400)

        # Layout principal
        layout = QtWidgets.QVBoxLayout()

        # Tabla para mostrar mesas
        self.table = QtWidgets.QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["N° Mesa", "Estado", "Capacidad"])
        layout.addWidget(self.table)

        # Botones
        btn_layout = QtWidgets.QHBoxLayout()
        self.btn_add = QtWidgets.QPushButton("Agregar Mesa")
        self.btn_edit = QtWidgets.QPushButton("Editar Mesa")
        self.btn_delete = QtWidgets.QPushButton("Eliminar Mesa")
        btn_layout.addWidget(self.btn_add)
        btn_layout.addWidget(self.btn_edit)
        btn_layout.addWidget(self.btn_delete)

        layout.addLayout(btn_layout)
        self.setLayout(layout)
