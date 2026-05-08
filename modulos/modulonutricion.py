import streamlit as st
# Importamos la función desde el archivo de cálculos
from modulos.calculos import calcular_macros

def mostrar_nutricion():
    st.title("🍎 Registro de Nutrición")
    
    # Ejemplo de uso real en la interfaz:
    alimento = st.selectbox("Selecciona alimento", ["Pechuga de Pollo", "Arroz Blanco"])
    peso = st.number_input("Gramos", value=100)
    cocido = st.checkbox("¿Está cocido?")
    
    if st.button("Calcular y guardar"):
        # 1. realizar el calculo con ña funcion que ya vimos
        res = calcular_macros (alimento, peso, es_cocido_=cocido)
        
        # 2. guardar automáticamente en la base de datos 
        exito =
        guardar_registro_comida(alimento, res['proteina'] res['kcal'])

    if exito:
        st.success(f"✅ registrado:
        {alimentos}, {res['proteina']}g p | {res['kcal']} kcal)") 
        st.info("los datos se han guardado en ru historial diario axon. ")
    else:
        st.error("hubo un problema al guardar el registro")
        
                      
  
