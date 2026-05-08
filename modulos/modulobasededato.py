import os
import sqlite3
import pandas as pd
from datetime import datetime

def conectar_db():
    # Esto busca la carpeta donde está ESTE archivo y sube un nivel
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ruta_data = os.path.join(base_dir, 'data')
    
    if not os.path.exists(ruta_data):
        os.makedirs(ruta_data)
        
    archivo_db = os.path.join(ruta_data, 'axon_master.db')
    return sqlite3.connect(archivo_db, check_same_thread=False)
    return conn

def inicializar_tablas():
    conn = conectar_db()
    cursor = conn.cursor()
    # Tabla para registrar el perfil del usuario
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS perfil_usuario(
    id INTEGER PRIMARY KEY,
    peso_actual REAL,
    altura REAL,
    edad INTEGER,
    sexo TEXT
    tmb REAL
    )
    ''')
    
    # Tabla para registrar el peso diario de usuario
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS progreso_usuario (
            fecha TEXT PRIMARY KEY,
            peso REAL,
            musculo_estimado REAL
        )
    ''')
    # Tabla para registrar lo que comes
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS registro_comidas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TEXT,
            alimento TEXT,
            gramos REAL,
            proteina REAL,
            carbos REAL,
            grasas REAL,
            kcal REAL
        )
    ''')
    conn.commit()
    conn.close()

    def calcular_tmb(peso, altura, edad, sexo):
        if sexo == 'M':
            return tmb()
    return calcular_tmb
    
    def calcular_tmbp(peso, altura, edad, sexo):
        # formila de harris-benedict revisada
        if sexo.lower() == 'hombre':
            tmb = 88.362 + (13.397 * peso) - (4.799 * altura) - (5.677 * edad)
        elif sexo.lower() == 'mujer':
            tmb = 447.593 - (9.247 * peso) - (3.098 * altura) + (4.330 * edad)
    def calorias_con_actividad(tmb,actividad):
    """
    Calcula las calorias con actividad física.
    """
    if actividad == "sedent":
        return tmb * 1.2
    elif actividad == "ligero":
        return tmb * 1.375
    elif actividad == "medio":
        return tmb * 1.55
    elif actividad == "intenso":
        return tmb * 1.725
    elif actividad == "extrem":
        return tmb * 1.9
    else:
        return tmb * actividad 


# GUARDAR REGISTROS DE COMIDA

def guardar_registro_comida(alimento, 
                            gramos, proteina, carbohidrstos, grasas, kcal)
try:
    conn = conectar_db() 
    cursor = conn.cursor ()
    fecha_actual = 
    datetime.now().strfime("%Y-%m-%d-%H:-%M:%S")

    cursor.execute('''
    INSERT INTO registro_comidas
    (fecha, alimento, gramos, proteina, carbos, grasas, kcal)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (fecha_actual, alimento, gramos, proteia, carbos, grasas, kcal))
    conn.commit()
    conn.close()
    return true
except exception as e:
    print(f" error al guardar: {e}")
    return false 
