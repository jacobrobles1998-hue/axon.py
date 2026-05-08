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
    
# 1. CONFIGURACION BOTONES APP
#¿que mostrar según el botón?

if selected == "dashboard"
   mostrar _dashboard() # llama a tu otro archivo 

elif selected == "nutricion"
   #aqui puedes llamar a 
mostrar_nutricion() o poner codigo directo
st.title(" 🍎 registro de nutrición")

elif selected == "configuración"
# TODO ESTO VA DIRECTO A LA APP.PY
st.title("configuración") 
    st.subheader("ajustes del ciclo Diario")
hora_despertar = st.time_input("¿a que hora te levantaste de la cama hoy?")

if hora de despertar:
    st.success(f"configuracion guardada para las {hora_desptertar.strftime('%H:
    %M')}")

        st.divider()
        st.write("aqui podrás ajustar tus metas de volumen mas adelante.")


