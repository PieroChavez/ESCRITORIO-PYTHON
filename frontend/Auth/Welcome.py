from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QColor, QPalette
from Auth.Login import LoginWindow
from Auth.Register import RegisterWindow

class WelcomeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bienvenido - Sistema de Pedidos")
        self.setGeometry(200, 200, 400, 400)  # Made window taller
        self.setStyleSheet("""
            QWidget {
                background-color: #f0f0f0;
            }
            QLabel {
                color: #2c3e50;
                font-size: 24px;
                font-weight: bold;
                margin: 20px;
            }
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 15px;
                margin: 10px 50px;
                border-radius: 5px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton#registerBtn {
                background-color: #2ecc71;
            }
            QPushButton#registerBtn:hover {
                background-color: #27ae60;
            }
        """)

        layout = QVBoxLayout()
        layout.setSpacing(20)
        layout.setContentsMargins(30, 40, 30, 40)

        # Welcome text
        label = QLabel("☕ BARISTAPOST")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setFont(QFont("Arial", 28, QFont.Weight.Bold))
        
        subtitle = QLabel("Sistema de Gestión de Café")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle.setStyleSheet("font-size: 16px; color: #7f8c8d; margin: 0px;")
        
        layout.addWidget(label)
        layout.addWidget(subtitle)
        layout.addSpacing(30)

        # Login Button
        self.btn_login = QPushButton("Iniciar Sesión")
        self.btn_login.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_login.clicked.connect(self.open_login)
        layout.addWidget(self.btn_login)

        # Register Button
        self.btn_register = QPushButton("Registrarse")
        self.btn_register.setObjectName("registerBtn")
        self.btn_register.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_register.clicked.connect(self.open_register)
        layout.addWidget(self.btn_register)

        layout.addStretch()
        self.setLayout(layout)

    def open_login(self):
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()

    def open_register(self):
        self.register_window = RegisterWindow()
        self.register_window.show()
        self.close()
