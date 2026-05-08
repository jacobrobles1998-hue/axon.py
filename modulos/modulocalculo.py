import streamlit as st

# ==========================================
# 1. BASE DE DATOS DE ALIMENTOS (LOGICA PRO)
# ==========================================


# Valores por cada 100g en CRUDO
BASE_ALIMENTOS = {
    # --- PROTEÍNAS ---
    "Pechuga de Pollo": {"tipo": "Proteína", "p": 23.1, "c": 0.0, "g": 1.2, "kcal": 110, "factor": 0.75},
    "Carne de Res Magra": {"tipo": "Proteína", "p": 21.5, "c": 0.0, "g": 4.5, "kcal": 135, "factor": 0.70},
    "Lomo de Cerdo": {"tipo": "Proteína", "p": 20.0, "c": 0.0, "g": 8.0, "kcal": 155, "factor": 0.72},
    "Pescado Blanco (Merluza)": {"tipo": "Proteína", "p": 19.0, "c": 0.0, "g": 2.0, "kcal": 95, "factor": 0.80},
    "Salmón": {"tipo": "Proteína", "p": 20.0, "c": 0.0, "g": 13.0, "kcal": 200, "factor": 0.82},
    "Huevos (Unidad ~50g)": {"tipo": "Proteína", "p": 6.3, "c": 0.6, "g": 5.0, "kcal": 78, "factor": 1.0},
    "Carne molida": {"tipo": "Proteína", "p": 20.0, "c": 0.0, "g": 8.0, "kcal": 155, "factor": 0.72},

    # --- PROTEÍNA EN POLVO (1 scoop ≈ 30g) ---
    "Optimum Nutrition Gold Standard Whey": {"tipo": "Proteína en Polvo", "p": 79.0, "c": 8.0, "g": 6.0, "kcal": 390, "factor": 1.0},
    "Dymatize ISO100": {"tipo": "Proteína en Polvo", "p": 83.0, "c": 3.0, "g": 1.0, "kcal": 370, "factor": 1.0},
    "MyProtein Impact Whey": {"tipo": "Proteína en Polvo", "p": 80.0, "c": 8.0, "g": 6.0, "kcal": 400, "factor": 1.0},
    "MuscleTech NitroTech": {"tipo": "Proteína en Polvo", "p": 76.0, "c": 10.0, "g": 7.0, "kcal": 410, "factor": 1.0},
    "Isopure Zero Carb": {"tipo": "Proteína en Polvo", "p": 83.0, "c": 1.0, "g": 1.0, "kcal": 360, "factor": 1.0},
    "Rule 1 R1 Whey Blend": {"tipo": "Proteína en Polvo", "p": 77.0, "c": 10.0, "g": 6.0, "kcal": 390, "factor": 1.0},
    "BSN Syntha-6": {"tipo": "Proteína en Polvo", "p": 47.0, "c": 32.0, "g": 13.0, "kcal": 425, "factor": 1.0},
    "Cellucor COR-Performance Whey": {"tipo": "Proteína en Polvo", "p": 77.0, "c": 9.0, "g": 6.0, "kcal": 385, "factor": 1.0},
    "GHOST Whey": {"tipo": "Proteína en Polvo", "p": 70.0, "c": 14.0, "g": 7.0, "kcal": 400, "factor": 1.0},
    "MusclePharm Combat Protein": {"tipo": "Proteína en Polvo", "p": 68.0, "c": 15.0, "g": 8.0, "kcal": 405, "factor": 1.0},
    "ProScience Whey Protein": {"tipo": "Proteína en Polvo", "p": 78.0, "c": 9.0, "g": 6.0, "kcal": 390, "factor": 1.0},
    
    # --- CARBOHIDRATOS COMPLEJOS ---
    "Arroz Blanco": {"tipo": "Carbo Complejo", "p": 7.0, "c": 78.0, "g": 0.6, "kcal": 350, "factor": 2.8},
    "Arroz Integral": {"tipo": "Carbo Complejo", "p": 7.5, "c": 72.0, "g": 2.5, "kcal": 345, "factor": 2.5},
    "Avena en Hojuelas": {"tipo": "Carbo Complejo", "p": 13.0, "c": 66.0, "g": 7.0, "kcal": 380, "factor": 2.0},
    "Pasta de Trigo": {"tipo": "Carbo Complejo", "p": 12.0, "c": 70.0, "g": 1.5, "kcal": 350, "factor": 2.3},
    "Papa / Patata": {"tipo": "Carbo Complejo", "p": 2.0, "c": 17.0, "g": 0.1, "kcal": 77, "factor": 1.0},
    "Batata / Camote": {"tipo": "Carbo Complejo", "p": 1.6, "c": 20.0, "g": 0.1, "kcal": 86, "factor": 0.95},
    "Lentejas": {"tipo": "Carbo Complejo", "p": 24.0, "c": 60.0, "g": 1.0, "kcal": 340, "factor": 2.4},
    "Manzana (Absorción Lenta)": {"tipo": "Carbo Complejo", "p": 0.3, "c": 14.0, "g": 0.2, "kcal": 52, "factor": 1.0},
    "Pera (Absorción Lenta)": {"tipo": "Carbo Complejo", "p": 0.4, "c": 15.0, "g": 0.1, "kcal": 57, "factor": 1.0},
    "Fresas / Frutos Rojos (Absorción Lenta)": {"tipo": "Carbo Complejo", "p": 0.7, "c": 8.0, "g": 0.3, "kcal": 33, "factor": 1.0},
    "Durazno / Melocotón (Absorción Lenta)": {"tipo": "Carbo Complejo", "p": 0.9, "c": 10.0, "g": 0.3, "kcal": 39, "factor": 1.0},
    
    # --- CARBOHIDRATOS SIMPLES ---
    "Plátano / Banano (Absorción Rápida)": {"tipo": "Carbo Simple", "p": 1.1, "c": 23.0, "g": 0.3, "kcal": 90, "factor": 1.0},
    "Sandía (Absorción Rápida)": {"tipo": "Carbo Simple", "p": 0.6, "c": 8.0, "g": 0.2, "kcal": 30, "factor": 1.0},
    "Uvas (Absorción Rápida)": {"tipo": "Carbo Simple", "p": 0.7, "c": 18.0, "g": 0.2, "kcal": 67, "factor": 1.0},
    "Piña (Absorción Rápida)": {"tipo": "Carbo Simple", "p": 0.5, "c": 13.0, "g": 0.1, "kcal": 50, "factor": 1.0},
    "Mango (Absorción Rápida)": {"tipo": "Carbo Simple", "p": 0.8, "c": 15.0, "g": 0.4, "kcal": 60, "factor": 1.0},
    # --- GASEOSAS (valores aprox por 100ml ≈ 100g) ---
    "Coca‑Cola": {"tipo": "Gaseosa", "p": 0.0, "c": 10.6, "g": 0.0, "kcal": 42, "factor": 1.0},
    "Coca‑Cola Zero": {"tipo": "Gaseosa", "p": 0.0, "c": 0.0, "g": 0.0, "kcal": 0, "factor": 1.0},
    "Pepsi": {"tipo": "Gaseosa", "p": 0.0, "c": 11.0, "g": 0.0, "kcal": 44, "factor": 1.0},
    "Pepsi Zero": {"tipo": "Gaseosa", "p": 0.0, "c": 0.0, "g": 0.0, "kcal": 0, "factor": 1.0},
    "Sprite": {"tipo": "Gaseosa", "p": 0.0, "c": 10.0, "g": 0.0, "kcal": 40, "factor": 1.0},
    "Sprite Zero": {"tipo": "Gaseosa", "p": 0.0, "c": 0.0, "g": 0.0, "kcal": 0, "factor": 1.0},
    "Fanta Naranja": {"tipo": "Gaseosa", "p": 0.0, "c": 11.0, "g": 0.0, "kcal": 45, "factor": 1.0},
    "7UP": {"tipo": "Gaseosa", "p": 0.0, "c": 10.3, "g": 0.0, "kcal": 41, "factor": 1.0},
    "Mountain Dew": {"tipo": "Gaseosa", "p": 0.0, "c": 12.6, "g": 0.0, "kcal": 50, "factor": 1.0},
    "Dr Pepper": {"tipo": "Gaseosa", "p": 0.0, "c": 10.4, "g": 0.0, "kcal": 41, "factor": 1.0},
    "Colombiana": {"tipo": "Gaseosa", "p": 0.0, "c": 11.0, "g": 0.0, "kcal": 44, "factor": 1.0},
    "Manzana Postobón": {"tipo": "Gaseosa", "p": 0.0, "c": 11.2, "g": 0.0, "kcal": 45, "factor": 1.0},
    "Uva Postobón": {"tipo": "Gaseosa", "p": 0.0, "c": 11.2, "g": 0.0, "kcal": 45, "factor": 1.0},
    "Gaseosa (Genérica)": {"tipo": "Gaseosa", "p": 0.0, "c": 11.0, "g": 0.0, "kcal": 42, "factor": 1.0},
    "Pan Tajado (Blanco/Integral)": {"tipo": "Carbo Simple", "p": 8.0, "c": 45.0, "g": 3.0, "kcal": 250, "factor": 1.0},
    "Miel de Abeja (100g)": {"tipo": "Carbo Simple", "p": 0.3, "c": 82.0, "g": 0.0, "kcal": 304, "factor": 1.0},
    "Azúcar Blanca (100g)": {"tipo": "Carbo Simple", "p": 0.0, "c": 100.0, "g": 0.0, "kcal": 387, "factor": 1.0},
    
    # --- GRASAS ---
    "Aceite de Oliva": {"tipo": "Grasa", "p": 0.0, "c": 0.0, "g": 100.0, "kcal": 884, "factor": 1.0},
    "Aguacate": {"tipo": "Grasa", "p": 2.0, "c": 8.5, "g": 15.0, "kcal": 160, "factor": 1.0},
    "Nueces / Almendras": {"tipo": "Grasa", "p": 20.0, "c": 21.0, "g": 50.0, "kcal": 600, "factor": 1.0},
    "Mantequilla de Maní": {"tipo": "Grasa", "p": 25.0, "c": 20.0, "g": 50.0, "kcal": 588, "factor": 1.0}
}
    
# ==========================================
# 2. FUNCIONES DE CÁLCULO
# ==========================================

def calcular_macros(alimento, gramos, es_cocido=False):
    """
    Calcula los macros exactos basándose en si el peso es crudo o cocido.
    """
    datos = BASE_ALIMENTOS.get(alimento)
    if not datos:
        return None
    # Si el usuario pesó la comida ya cocida, ajustamos al equivalente en crudo
    # coeficinets de conversion aproximados
# crudo a cocido: arroz (x3), carne (x0.75), lentejas (x2.5), 
conversiones = {
    'arroz': 3,
    'carne': 0.75,
    'lentejas': 2.5,
    'huevos': 1.0 # el huevo no varia significativamente

}
def convertir_a_crudo(alimetos, gramos, estado):
    if estado.lower() == 'cocido':
        coef = conversiones.get(alimetos, 1)
        gramos_equivalentes = gramos / coef
    else:
            gramos_equivalentes = gramos
            
            # ahora usamos esa variable para calcular los macros
            ratio = gramos_equivalentes / 100
            return {
                "proteina": round(datos["p"] * ratio, 1),
                "carbo": round(datos["c"] * ratio, 1),
                "grasa": round(datos["g"] * ratio, 1),
                "kcal": round(datos["kcal"] * ratio, 1)
                }
            
def tasa_metabolica_basal(peso, altura, edad, sexo="Masculino"):
    """
    Fórmula de Harris-Benedict para saber cuánto quemas sentado.
    """
    if sexo == "Masculino":
        return 88.36 + (13.4 * peso) + (4.8 * altura) - (5.7 * edad)
    else:
        return 447.59 + (9.2 * peso) + (3.1 * altura) - (4.3 * edad)
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

# para saber que quiere el usuario ( superavit, defitic, mantenimiento)
        
