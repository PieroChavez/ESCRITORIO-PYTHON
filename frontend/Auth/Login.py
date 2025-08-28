# Auth/Login.py
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from Home.index import HomeWindow  # 👈 Importa tu Home

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login - BaristaPost")
        self.setGeometry(200, 200, 400, 300)

        layout = QVBoxLayout()

        self.label = QLabel("Inicia Sesión")
        layout.addWidget(self.label)

        self.input_user = QLineEdit()
        self.input_user.setPlaceholderText("Usuario")
        layout.addWidget(self.input_user)

        self.input_pass = QLineEdit()
        self.input_pass.setPlaceholderText("Contraseña")
        self.input_pass.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.input_pass)

        self.btn_login = QPushButton("Entrar")
        self.btn_login.clicked.connect(self.check_login)
        layout.addWidget(self.btn_login)

        self.setLayout(layout)

    def check_login(self):
        username = self.input_user.text()
        password = self.input_pass.text()

        # 🔹 Aquí deberías validar contra tu base de datos
        if username == "admin" and password == "1234":  # Ejemplo temporal
            QMessageBox.information(self, "Éxito", "Login correcto")

            # Abrir Home
            self.home = HomeWindow()
            self.home.show()

            self.close()  # Cierra la ventana de login
        else:
            QMessageBox.warning(self, "Error", "Usuario o contraseña incorrectos")
