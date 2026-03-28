import pandas as pd

def calcular_atribucion_last_click(df_ventas):
    # En este modelo, el canal en ventas.csv es el que se lleva el 100%
    return df_ventas.groupby('Canal')['Monto'].sum().reset_index()

def calcular_metricas_rentabilidad(df_ventas, presupuesto_dict):
    """
    presupuesto_dict: {'Facebook': 500, 'Google': 300, ...}
    """
    resumen = df_ventas.groupby('Canal').agg(
        Ventas_Totales=('Monto', 'sum'),
        Cantidad_Ventas=('ID_Venta', 'count')
    ).reset_index()
    
    # Mapear el costo invertido por canal
    resumen['Inversion'] = resumen['Canal'].map(presupuesto_dict).fillna(0)
    
    # ROI: (Ingreso - Inversion) / Inversion
    resumen['ROI'] = (resumen['Ventas_Totales'] - resumen['Inversion']) / resumen['Inversion']
    
    # CPA: Inversion / Cantidad de Ventas
    resumen['CPA'] = resumen['Inversion'] / resumen['Cantidad_Ventas']
    
    return resumen
