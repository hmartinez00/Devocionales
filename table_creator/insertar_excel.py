import pandas as pd


archivo = 'backup/lectura 52 semanas.doc.xlsx'

df = pd.read_excel(archivo, sheet_name='Hoja3')

print(df)