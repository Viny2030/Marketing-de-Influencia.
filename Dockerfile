FROM python:3.10-slim

WORKDIR /app

# Instalamos dependencias del sistema necesarias para PostgreSQL (psycopg2)
RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Exponemos ambos puertos (8000 para API, 8501 para Streamlit)
EXPOSE 8000
EXPOSE 8501
