"""
Projeto final

Alexia Naara
Iago Campelo
"""

# Importação dos módulos
import pandas as pd
from matplotlib import pyplot as plt
import io

df = pd.read_csv('Students_data.csv')
media = df.drop(columns=['class','GPA','ID','race','from1','from2','from3','from4','gender','y'])
aprovados = df['y']
print(aprovados)
