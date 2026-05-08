import streamlit as st

def aplicar_estilos_axon():
    # Definimos tus colores de marca
    AXON_CYAN = "#00D1FF"
    AXON_DARK = "#02060E"
    AXON_SALMON = "#FA8072"

    st.markdown(f"""
        <style>
        /* Fondo con el gradiente que te gusta */
        .stApp {{ 
            background-color: {AXON_DARK};
            background-image: radial-gradient(circle at 20% 0%, rgba(197, 3, 55, 0.55) 0%, rgba(2, 6, 14, 0) 55%);
            background-attachment: fixed;
        }}
        
        /* Estilos para textos y títulos */
        label, h1, h2, h3, p {{ color: #FFFFFF !important; font-family: 'Courier New', monospace; }}
        
        /* Ocultar barra lateral por defecto */
        [data-testid="stSidebar"] {{ display: none; }}
        
        /* Margen para que la barra de abajo no tape nada */
        .block-container {{ padding-bottom: 100px; }}
        </style>
    """, unsafe_allow_html=True)