from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QComboBox
)
from PyQt6.QtCore import Qt
from Service.Api import register_user

class RegisterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registrar nuevo usuario")
        self.setGeometry(400, 200, 350, 380)

        layout = QVBoxLayout()

        title = QLabel("Registro de Usuario")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(title)

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Correo electrónico")
        layout.addWidget(self.email_input)

        self.telefono_input = QLineEdit()
        self.telefono_input.setPlaceholderText("Teléfono")
        layout.addWidget(self.telefono_input)

        self.tipo_doc = QComboBox()
        self.tipo_doc.addItems(["DNI", "RUC10", "RUC20"])
        layout.addWidget(self.tipo_doc)

        self.numero_doc_input = QLineEdit()
        self.numero_doc_input.setPlaceholderText("Número de documento")
        layout.addWidget(self.numero_doc_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Contraseña")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password_input)

        self.role_input = QComboBox()
        self.role_input.addItems(["cliente", "negocio", "repartidor"])
        layout.addWidget(self.role_input)

        self.register_btn = QPushButton("Registrar")
        self.register_btn.clicked.connect(self.send_register)
        layout.addWidget(self.register_btn)

        self.setLayout(layout)

    def send_register(self):
        from Auth.Login import LoginWindow  # ✅ Importación diferida

        data = {
            "email": self.email_input.text(),
            "telefono": self.telefono_input.text(),
            "tipo_documento": self.tipo_doc.currentText(),
            "numero_documento": self.numero_doc_input.text(),
            "password": self.password_input.text(),
            "role": self.role_input.currentText()
        }

        if not all(data.values()):
            QMessageBox.warning(self, "Campos incompletos", "Por favor, completa todos los campos.")
            return

        response = register_user(data)

        if response is None:
            QMessageBox.critical(self, "Error de conexión", "No se pudo conectar al servidor.")
            return

        if response.status_code == 201:
            QMessageBox.information(self, "Éxito", "Usuario registrado correctamente.")
            self.close()
            self.login_window = LoginWindow()
            self.login_window.show()
        elif response.status_code == 409:
            QMessageBox.warning(self, "Ya registrado", "El número de documento ya está registrado.")
        else:
            error = response.json().get("error", "Error desconocido")
            QMessageBox.warning(self, "Error", f"No se pudo registrar: {error}")
