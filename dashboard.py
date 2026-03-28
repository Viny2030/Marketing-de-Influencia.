import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Marketing Dashboard", layout="wide")
st.title("📊 Attribution Dashboard")

# URL CRÍTICA: 'api' es el nombre del servicio en docker-compose
URL_API = "http://api:8000/report"

try:
    response = requests.get(URL_API)
    if response.status_code == 200:
        res = response.json()
        if res:
            # Convertimos el diccionario {campaña: valor} a DataFrame
            df = pd.DataFrame(list(res.items()), columns=['Campaña', 'Revenue'])
            
            st.subheader("💰 Revenue por campaña")
            st.bar_chart(df.set_index('Campaña'))
            st.table(df)
        else:
            st.warning("La API no devolvió datos. ¿Corriste el procesador?")
    else:
        st.error(f"Error en la API: {response.status_code}")
except Exception as e:
    st.error(f"No se pudo conectar con la API en {URL_API}")
    st.info("Error técnico: " + str(e))
