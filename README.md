# ☕ Sistema de Ventas de Café

Proyecto para un sistema integral de ventas de café, con:
- **Backend** en FastAPI (API REST)
- **Frontend** como app de escritorio en PyQt6

Permite gestionar pedidos en tienda y online, con autenticación de baristas y control de inventario.

---

## 📁 Estructura del proyecto

- **USA UN ENTORNO VIRTUAL**

**🚀 1) Definir las funcionalidades principales**

🔹 Autenticación y registro de usuarios/baristas

Registrar quién atiende (empleado/barista).

API para validar credenciales.

🔹 Gestión de productos

Catálogo de cafés, métodos, accesorios, etc.

Precios dinámicos.

🔹 Pedidos en tienda y online

En escritorio: generar tickets/boletas.

En app móvil: elegir productos, pagar y seguir el estado del pedido.

🔹 Pagos

Integrar pasarelas como Culqi, Niubiz o Stripe.

🔹 Inventario

Reducir stock en tiempo real con cada venta.

🔹 Reportes

Ventas por día/semana/mes.

Productos más vendidos.

🔹 Notificaciones

Avisar a clientes cuando su pedido esté listo.

**🖥️ 2) Aplicación de escritorio**

Lenguaje: Python.

Framework para GUI:

PyQt5 / PyQt6 (muy profesional).

O alternativamente, Tkinter si buscas algo sencillo.

Comunicación con el backend: API REST (por ejemplo, usando requests en Python).

**📱 3) Aplicación móvil**

Puedes crearla con:

Kivy (Python, multiplataforma).

Flutter o React Native (más profesional, pero necesitarás usar Dart/JavaScript).

**🌐 4) Backend con APIs REST**

Lenguaje recomendado: Python (con Flask o FastAPI).

Base de datos: PostgreSQL o MySQL.

Endpoints que necesitarás:

/auth/login y /auth/register

/products para CRUD de productos.

/orders para crear/actualizar pedidos.

/inventory para control de stock.

/reports para estadísticas.

**🏦 5) Infraestructura y despliegue**

Alojamiento en un VPS o servicios como Railway, Render o AWS.

Base de datos en la nube (p. ej., PostgreSQL en Supabase o Neon).

Certificados SSL para seguridad (HTTPS).

**🔐 6) Seguridad**

Autenticación con tokens JWT.

Validar roles (empleados, admin).

Encriptar contraseñas.

**🔄 7) Flujo de trabajo recomendado**

1️⃣ Diseña un mockup de tus pantallas principales (tanto para escritorio como móvil).

2️⃣ Crea el backend con Flask/FastAPI, define tu base de datos y APIs REST.

3️⃣ Desarrolla la app de escritorio:

PyQt: ventanas para login, catálogo, carrito, pedidos, reportes.

Conexión a APIs usando requests.

4️⃣ Desarrolla la app móvil:

Kivy para reutilizar código en Python, o Flutter/React Native si quieres una experiencia más moderna.

5️⃣ Integra pasarela de pago y pruebas con pedidos reales.

6️⃣ Despliega el backend y prueba todo el flujo end-to-end.

**🔨 Tecnologías sugeridas**

✅ Frontend escritorio: PyQt6
✅ Frontend móvil: Kivy (o Flutter si estás abierta a otro lenguaje)
✅ Backend: FastAPI (rápido, moderno)
✅ DB: PostgreSQL
✅ API client: requests en Python
✅ Control de versiones: Git + GitHub
✅ Despliegue: Railway / Render / VPS

--------------------------------------------------------------------

🟢 1) Configurar entorno virtual (recomendado)
 **EN UNA CONSOLO PEGAR:**
 python -m venv venv

 🔵 2) Instalar dependencias para el backend con FastAPI
    pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic python-dotenv

 🔴 3) Instalar dependencias para la aplicación de escritorio con PyQt6
     pip install PyQt6 requests

**####################################################################**
## AQUI INICIAMOS EL BACK

✅ Paso : Reinicia tu servidor
Desde la carpeta backend/:

-- python -m app.app -- BACK

-- python main.py -- FROND


