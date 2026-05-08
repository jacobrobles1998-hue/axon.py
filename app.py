import streamlit as st
from streamlit_option_menu import option_menu

# 1. Traemos las piezas de la carpeta 'modulos'
from modulos.moduloestilos import aplicar_estilos_axon
from modulos.modulodashboard import mostrar_dashboard
from modulos.modulobasededato import inicializar_tablas

# 2. Arrancamos la App (Configuración)
st.set_page_config(page_title="AXON", layout="wide", initial_sidebar_state="collapsed")

# 3. Activamos la base de datos y el diseño
inicializar_tablas()
aplicar_estilos_axon()

# 4. El Menú (Lo que tú ves)
selected = option_menu(
    menu_title=None,
    options=["Dashboard", "Nutrición", "configuración"],
    icons=["house", "egg-fried", "activity"],
    orientation="horizontal"
)

# 5. ¿Qué mostrar según el botón?
if selected == "Dashboard":
    mostrar_dashboard()
