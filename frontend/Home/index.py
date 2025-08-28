# frontend/Home/index.py
from PyQt6.QtWidgets import (QMainWindow, QLabel, QWidget, QVBoxLayout, 
                            QHBoxLayout, QPushButton, QStackedWidget, QGridLayout)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QFont

class HomeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BaristaPost - Panel Principal")
        self.setGeometry(100, 100, 1200, 700)
        
        # Widget principal
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        
        # Layout principal
        layout = QHBoxLayout(main_widget)
        
        # Panel lateral (menú)
        sidebar = QWidget()
        sidebar.setFixedWidth(200)
        sidebar_layout = QVBoxLayout(sidebar)
        
        # Título del menú
        menu_title = QLabel("MENÚ PRINCIPAL")
        menu_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        sidebar_layout.addWidget(menu_title)
        
        # Botones del menú
        self.create_menu_button("🪑 Mesas", sidebar_layout, self.show_mesas)
        self.create_menu_button("📝 Pedidos", sidebar_layout, self.show_pedidos)
        self.create_menu_button("🧾 Tickets", sidebar_layout, self.show_tickets)
        self.create_menu_button("📦 Almacén", sidebar_layout, self.show_almacen)
        
        # Agregar espacio al final
        sidebar_layout.addStretch()
        
        # Botón de cerrar sesión
        logout_btn = QPushButton("🚪 Cerrar Sesión")
        logout_btn.clicked.connect(self.logout)
        sidebar_layout.addWidget(logout_btn)
        
        # Área principal de contenido
        self.content_area = QStackedWidget()
        
        # Agregar páginas al área de contenido
        self.setup_mesas_page()
        self.setup_pedidos_page()
        self.setup_tickets_page()
        self.setup_almacen_page()
        
        # Agregar widgets al layout principal
        layout.addWidget(sidebar)
        layout.addWidget(self.content_area)

    def create_menu_button(self, text, layout, slot):
        button = QPushButton(text)
        button.setFixedHeight(50)
        button.clicked.connect(slot)
        layout.addWidget(button)
        return button

    def setup_mesas_page(self):
        mesas_widget = QWidget()
        layout = QVBoxLayout(mesas_widget)
        
        # Título de la sección
        title = QLabel("Gestión de Mesas")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size: 24px; margin: 20px;")
        layout.addWidget(title)

        # Grid para las mesas
        grid_layout = QGridLayout()
        
        # Crear 6 mesas (2 filas x 3 columnas)
        for i in range(6):
            mesa_widget = QWidget()
            mesa_layout = QVBoxLayout(mesa_widget)
            
            # Icono/Número de mesa
            mesa_label = QLabel(f"Mesa {i + 1}")
            mesa_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            mesa_label.setStyleSheet("""
                font-size: 18px;
                padding: 20px;
                background-color: #3498db;
                color: white;
                border-radius: 10px;
            """)
            
            # Estado de la mesa
            estado_label = QLabel("Disponible")
            estado_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            estado_label.setStyleSheet("color: #27ae60; font-weight: bold;")
            
            # Botón de acciones
            btn_acciones = QPushButton("Ver Detalles")
            btn_acciones.clicked.connect(lambda checked, num=i+1: self.gestionar_mesa(num))
            
            mesa_layout.addWidget(mesa_label)
            mesa_layout.addWidget(estado_label)
            mesa_layout.addWidget(btn_acciones)
            
            # Añadir al grid (2 filas x 3 columnas)
            grid_layout.addWidget(mesa_widget, i // 3, i % 3)

        layout.addLayout(grid_layout)
        self.content_area.addWidget(mesas_widget)

    def gestionar_mesa(self, numero_mesa):
        # Aquí puedes agregar la lógica para gestionar cada mesa
        print(f"Gestionando Mesa {numero_mesa}")
        # Por ejemplo: abrir un diálogo con opciones para:
        # - Tomar pedido
        # - Ver pedidos actuales
        # - Cerrar mesa
        # - Cambiar estado

    def setup_pedidos_page(self):
        pedidos_widget = QWidget()
        layout = QVBoxLayout(pedidos_widget)
        layout.addWidget(QLabel("Gestión de Pedidos"))
        # Aquí agregarás el contenido de la página de pedidos
        self.content_area.addWidget(pedidos_widget)

    def setup_tickets_page(self):
        tickets_widget = QWidget()
        layout = QVBoxLayout(tickets_widget)
        layout.addWidget(QLabel("Gestión de Tickets"))
        # Aquí agregarás el contenido de la página de tickets
        self.content_area.addWidget(tickets_widget)

    def setup_almacen_page(self):
        almacen_widget = QWidget()
        layout = QVBoxLayout(almacen_widget)
        layout.addWidget(QLabel("Gestión de Almacén"))
        # Aquí agregarás el contenido de la página de almacén
        self.content_area.addWidget(almacen_widget)

    def show_mesas(self):
        self.content_area.setCurrentIndex(0)

    def show_pedidos(self):
        self.content_area.setCurrentIndex(1)

    def show_tickets(self):
        self.content_area.setCurrentIndex(2)

    def show_almacen(self):
        self.content_area.setCurrentIndex(3)

    def logout(self):
        # Aquí implementarás la lógica de cierre de sesión
        self.close()
