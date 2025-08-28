# test_db.py - Script de prueba de conexión

from db import get_connection

def probar_conexion():
    print("🔍 Iniciando prueba de conexión a la base de datos...")
    
    conexion = get_connection()
    
    if conexion:
        print("✅ Conexión exitosa a la base de datos")
        print(f"   Host: {conexion.server_host}")
        print(f"   Usuario: {conexion.user}")
        print(f"   Base de datos: {conexion.database}")
        
        # Opcional: Mostrar bases de datos disponibles
        cursor = conexion.cursor()
        cursor.execute("SELECT DATABASE();")
        db_actual = cursor.fetchone()[0]
        print(f"   Base de datos seleccionada: {db_actual}")
        
        cursor.execute("SHOW TABLES;")
        tablas = cursor.fetchall()
        if tablas:
            print("   Tablas encontradas:")
            for tabla in tablas:
                print(f"     - {tabla[0]}")
        else:
            print("   ⚠️  No hay tablas en la base de datos.")
        
        conexion.close()
        print("   Conexión cerrada.")
    else:
        print("❌ No se pudo conectar a la base de datos.")
        print("   Revisa: host, usuario, contraseña o que MySQL esté en ejecución.")

if __name__ == "__main__":
    probar_conexion()