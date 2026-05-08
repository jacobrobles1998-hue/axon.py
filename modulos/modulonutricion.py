import streamlit as st
# Importamos la función desde el archivo de cálculos
from modulos.calculos import calcular_macros

def mostrar_nutricion():
    st.title("🍎 Registro de Nutrición")
    
    # Ejemplo de uso real en la interfaz:
    alimento = st.selectbox("Selecciona alimento", ["Pechuga de Pollo", "Arroz Blanco"])
    peso = st.number_input("Gramos", value=100)
    cocido = st.checkbox("¿Está cocido?")
    
    if st.button("Calcular"):
        res = calcular_macros(alimento, peso, es_cocido=cocido)
        st.success(f"Resultado: {res['proteina']}g Proteína | {res['kcal']} Kcal")