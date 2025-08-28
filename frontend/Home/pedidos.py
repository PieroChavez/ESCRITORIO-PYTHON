from PyQt5 import QtWidgets, QtCore

class PedidosWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BaristaPost - Gestión de Pedidos")
        self.setGeometry(200, 200, 600, 400)

        layout = QtWidgets.QVBoxLayout()

        # Tabla de pedidos
        self.table = QtWidgets.QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID Pedido", "Mesa", "Estado", "Total"])
        layout.addWidget(self.table)

        # Botones
        btn_layout = QtWidgets.QHBoxLayout()
        self.btn_new = QtWidgets.QPushButton("Nuevo Pedido")
        self.btn_update = QtWidgets.QPushButton("Actualizar Estado")
        self.btn_delete = QtWidgets.QPushButton("Eliminar Pedido")
        btn_layout.addWidget(self.btn_new)
        btn_layout.addWidget(self.btn_update)
        btn_layout.addWidget(self.btn_delete)

        layout.addLayout(btn_layout)
        self.setLayout(layout)
