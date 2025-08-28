from flask import Blueprint, request, jsonify
from app.db import get_connection
import bcrypt
from datetime import datetime

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    # lógica como ya la tienes
    pass

@auth_bp.route('/login', methods=['POST'])
def login():
    # lógica de login
    pass
