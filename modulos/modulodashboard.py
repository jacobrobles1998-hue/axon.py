import streamlit as st

def mostrar_dashboard():
    st.title("🚀 AXON - DASHBOARD")
    st.subheader("Estado Actual: Jacob")
    
    # Ejemplo de métricas rápidas
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Peso Objetivo", value="80 kg", delta="En proceso")
    with col2:
        st.metric(label="Proteína Hoy", value="120g / 180g")
    with col3:
        st.metric(label="Estado", value="Volumen Limpio")