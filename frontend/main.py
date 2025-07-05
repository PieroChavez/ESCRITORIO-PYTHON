import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QMessageBox
)
from PyQt6.QtCore import Qt

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login - Sistema de Ventas de Café")
        self.setGeometry(400, 200, 350, 200)

        layout = QVBoxLayout()

        # Título
        title_label = QLabel("Iniciar sesión")
        title_label.setStyleSheet("font-size: 20px; font-weight: bold;")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)

        # Campo de usuario
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Usuario")
        layout.addWidget(self.username_input)

        # Campo de contraseña
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Contraseña")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password_input)

        # Botón de login
        login_button = QPushButton("Iniciar sesión")
        login_button.clicked.connect(self.handle_login)
        layout.addWidget(login_button)

        self.setLayout(layout)

    def handle_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        # Validación básica
        if not username or not password:
            QMessageBox.warning(self, "Error", "Completa todos los campos")
            return

        # Aquí pondremos la llamada al backend. Por ahora simularemos:
        if username == "admin" and password == "1234":
            QMessageBox.information(self, "Éxito", "¡Inicio de sesión correcto!")
            self.open_dashboard()
        else:
            QMessageBox.critical(self, "Error", "Usuario o contraseña incorrectos")

    def open_dashboard(self):
        # Por ahora solo cerramos login y mostramos un mensaje de ejemplo
        self.close()
        self.dashboard = DashboardWindow()
        self.dashboard.show()

class DashboardWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dashboard - Sistema de Ventas de Café")
        self.setGeometry(400, 200, 500, 300)

        layout = QVBoxLayout()
        label = QLabel("Bienvenido al Dashboard del sistema de ventas de café ☕")
        label.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(label)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
