import streamlit as st

def mostrar_dashboard():
    st.title("🚀 AXON - DASHBOARD")
    st.subheader("Estado Actual: Jacob")

# 1. CONFIGURACION BOTONES APP
#¿que mostrar según el botón?

if selected == "dashboard"
   mostrar _dashboard() # llama a tu otro archivo 

elif selected == "nutricion"
   #aqui puedes llamar a 
mostrar_nutricion() o poner codigo directo
st.title("registro de nutrición")

elif selected == "configuración"
# TODO ESTO VA DIRECTO A LA APP.PY
st.title("configuración") 
    st.subheader("ajustes del ciclo Diario")
hora_despertar = st.time_input("¿a que hora te levantaste de la cama hoy?")

if hora de despertar :
     st.success(f"configuracion guardada para las {hora_desptertar.strftime('%H:
     %M')}")

         st.divider()
         st.write("aqui podrás ajustar tus metas de volumen mas adelante.")
                                                                                             
    # Ejemplo de métricas rápidas
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Peso Objetivo", value="80 kg", delta="En proceso")
    with col2:
        st.metric(label="Proteína Hoy", value="120g / 180g")
    with col3:
        st.metric(label="Estado", value="Volumen Limpio")
