import pandas as pd

data = pd.read_csv('/home/cris/Documentos/curso-ciencia-datos/archive/StudentsPerformance.csv')
print(data.head())

data.rename(columns={
    'gender': 'Genero',
    'math score': 'Calificacion de Matematicas',
}, inplace= True)
print(data.head())