# frontend/main.py
import sys
import os
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from Auth.Welcome import WelcomeWindow

def main():
    app = QApplication(sys.argv)
    
    # Global application styles
    app.setStyle('Fusion')  # Modern style base
    
    # Global stylesheet for the entire application
    app.setStyleSheet("""
        QWidget {
            background-color: #f0f0f0;
            font-family: Arial;
        }
        QLabel {
            color: #2c3e50;
            font-size: 14px;
        }
        QPushButton {
            background-color: #3498db;
            color: white;
            border: none;
            padding: 10px;
            margin: 5px;
            border-radius: 5px;
            font-size: 14px;
            min-width: 120px;
        }
        QPushButton:hover {
            background-color: #2980b9;
        }
        QLineEdit {
            padding: 8px;
            border: 2px solid #bdc3c7;
            border-radius: 5px;
            background-color: white;
            font-size: 14px;
        }
        QLineEdit:focus {
            border: 2px solid #3498db;
        }
        QMessageBox {
            background-color: #f0f0f0;
        }
        QMessageBox QPushButton {
            min-width: 80px;
        }
    """)

    window = WelcomeWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
