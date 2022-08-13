# coding=utf-8

# Projeto de ciencia de dados

# Joao tem um restaurante e esta precisando de ajuda para entender por que o fluxo de clientes anda baixo em horários suspostamente mais movimentados. 
# Voce, como cientista de dados, propõe-se a ajudar e João te entrega uma amostra de dados de ocupação do estabelecimento.
# Analise os dados do restaurante de João e descreva de forma simples uma possível causa da baixa ocupação em horários de pico.

# Importando os módulos necessários
import matplotlib.pyplot as plt # Módulo de geração de gráficos
import pandas as pd # Módulo de manipulação de tabelas

# Construindo o link de importação dos dados do restaurante de João
url='https://drive.google.com/file/d/1QWHUHWhcW-EiL6PX94AmVipaVmK6ZDxN/view?usp=sharing'
file_id=url.split('/')[-2]
dwn_url='https://drive.google.com/uc?id=' + file_id

# Download dos dados do restaurante
df = pd.read_csv(dwn_url)

# Mostrar linhas inicias da tabela
print(df.head())

# Figura onde o gráfico será construido
fig = plt.figure()

# Adicionar os eixos do gráfico
ax = fig.add_axes([0,0,1,1])

# Armazenando os dados de horas na variável hora
hora = df['hora']

# Armazenando os dados de ocupação na variável ocupacao
ocupacao = df['ocupacao']

# Uso do gráfico de barras
ax.bar(hora, ocupacao)

# Rótulo do eixo x
plt.xlabel("Hora")

# Rótulo do eixo y
plt.ylabel("Ocupação")

# Título do gráfico
plt.title("Ocupação por hora", fontsize=20)

# Aumentar tamanho da fonte dos rótulos dos eixos x e y
plt.rc('axes', labelsize=30)

# Aumentar tamanho da fonte dos elementos do eixo x
plt.rc('xtick', labelsize=30)

# Aumentar tamanho da fonte dos elementos do eixo y
plt.rc('ytick', labelsize=30)

# Mostrar o gráfico
plt.show()
