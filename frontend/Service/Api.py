# frontend/service/api.py

import requests

API_URL = "http://127.0.0.1:5000"  # Asegúrate de que el backend esté corriendo

def register_user(data: dict):
    try:
        response = requests.post(f"{API_URL}/register", json=data)
        return response
    except requests.exceptions.RequestException as e:
        print("❌ Error al conectar con el backend:", e)
        return None

def login_user(email: str, password: str):
    try:
        response = requests.post(f"{API_URL}/login", json={
            "email": email,
            "password": password
        })
        return response
    except requests.exceptions.RequestException as e:
        print("❌ Error al conectar con el backend:", e)
        return None
