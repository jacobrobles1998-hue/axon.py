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

    
# 1. CONFIGURACION BOTONES APP
#¿que mostrar según el botón?

if selected == "dashboard"
   mostrar _dashboard() # llama a tu otro archivo 

elif selected == "nutricion"
   #aqui puedes llamar a 
mostrar_nutricion() o poner codigo directo
st.title(" 🍎 registro de nutrición")

elif selected == "configuración"
# 1. BLOQUE DE DATOS METABOLICO (LO QUE VA A APARECER DE PRIMERO)
st.subheader("datos del usuario y tasa metabolica")
# campo de texto para el nombre 
usuario = st.text_input("SUJETO:" , placeholder="EJ: USUARIO 1")
#seleccion de sexo
sexo = st.radio.("SEXO:", ["MASCULINO" , "FEMENINO"], horizontal=true)
#edad y altura en columnas 
c1, c2 = st.columns(2)
with c1:
    edad = st.number_input("EDAD:", 
                           min_value=1, value=27) # coloque 27 por defecto
 with c2:
    altura = st.number _input("ALTURA (CM):",min_value=1, value=171) 
        #lo coloque por defecto

    
                           
        
                                
    
# TODO ESTO VA DIRECTO A LA APP.PY
st.title("configuración") 
    st.subheader("ajustes del ciclo Diario")
hora_despertar = st.time_input("¿a que hora te levantaste de la cama hoy?")

if hora de despertar:
    st.success(f"configuracion guardada para las {hora_desptertar.strftime('%H:
    %M')}")

        st.divider()
        st.write("aqui podrás ajustar tus metas de volumen mas adelante.")


