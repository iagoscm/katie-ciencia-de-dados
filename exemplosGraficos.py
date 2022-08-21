import numpy as np
import matplotlib as mpl
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import plotly.express as px

from os import path
from PIL import Image
from google.colab import drive

from urllib.request import urlopen
import json

# --- Gráfico de Barras ---

# Conjunto de dados
dados = {'materias': ["Cálculo", "PAA", "Lógica", "P1", "S.O"], 'alunos': [60, 20, 40, 52, 36]}
df = pd.DataFrame(dados)

# Plotando gráfico de barras
plt.figure(figsize=(10,5))
plt.bar(df['materias'], df['alunos'])
plt.title("Disposição de alunos da graduação")
plt.xlabel("Máterias")
plt.ylabel("Alunos")
plt.show()

# --- Gráfico de Linhas ---

velocidade = [10, 18, 22, 30, 50, 55, 78, 85, 100, 150]
tempo = [1,2,3,4,5,6,7,8,9,10]

plt.figure(figsize=(10,5))
plt.plot(tempo, velocidade, 'r')
plt.title("Gráfico de linha")
plt.xlabel("Tempo")
plt.ylabel("KM/h")
#plot = plt.gca()
plt.show()

# --- Gráfico de Área ---

velocidade2 = [10, 18, 22, 30, 50, 55, 78, 85, 100, 150]
x = range(0,10)
plt.figure(figsize=(10,5))
plt.stackplot(x, velocidade1,velocidade2, labels=['loja A','loja B'])
plt.legend(loc='upper left')
plt.title("Vendas por tempo")
plt.xlabel("meses")
plt.ylabel("Unidades vendidas")
plt.show()

# --- Histograma ---

seed = np.random.default_rng(123456)
dist1 = seed.standard_normal(10000)
plt.figure(figsize=(12,6))
plt.hist(dist1)
plt.title("Histograma")
plt.show()

notas = [8, 7, 7, 6, 5, 2, 5, 6, 2, 2, 3, 4, 5, 6, 10, 9, 10, 1, 4,7,7]
plt.figure(figsize=(12,6))
plt.hist(notas, color='orange')
plt.title("Histograma")
plt.xlabel("Notas")
plt.show()
plt.figure(figsize=(12,6))
sns.histplot(notas)
plt.title("Histograma")
plt.xlabel("Notas")
plt.show()

# --- Gráfico de Pizza ---

labels = 'Banana', 'Maçã', 'Laranja', 'Limão'
sizes = [15, 30, 45, 10]
explode = (0, 0, 0.1, 0)

plt.figure(figsize=(12,6))
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%')
plt.title("Porcentagem de vendas")
plt.savefig("")
plt.show()

# --- Gráfico de Scatter/Dispersão ---

# Carregando dados
tips = sns.load_dataset("tips")

# Plotando gráfico de dispersão
plt.figure(figsize=(12,6))
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time")
plt.title("Gráfico de dispersão")
plt.show()

np.random.seed(123456)
N = 50
x = np.random.rand(N)
y = np.random.rand(N)
plt.figure(figsize=(10,6))
plt.scatter(x, y)
plt.show()

# --- Gráfico de Caixa (Box-plot) ---

plt.figure(figsize=(8,8))
plt.boxplot(notas)
plt.title("Avaliação AB1 Data vis")
plt.ylabel("Notas")
plt.show()

plt.figure(figsize=(12,6))
sns.boxplot(x="day", y="total_bill", data=tips)
plt.show()

# --- Pairplot ---

penguins = sns.load_dataset("penguins")
sns.pairplot(penguins)
plt.show()

# --- Heatmap ---

plt.figure(figsize=(12,6))
sns.heatmap(penguins.corr(), annot = True)
plt.show()

# --- Bubbleplot ---

colors = np.random.rand(N)
print(colors)
area = (30 * np.random.rand(N))**2

plt.figure(figsize=(10,6))
plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()

# --- Gráfico de Mapa (Mapplot) ---

with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
                   dtype={"fips": str})


fig = px.choropleth(df, geojson=counties, locations='fips', color='unemp',
                           color_continuous_scale="Viridis",
                           range_color=(0, 12),
                           scope="usa",
                           labels={'unemp':'unemployment rate'}
                          )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
