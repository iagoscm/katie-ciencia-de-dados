"""
Building a Time Series Weather Forecasting Application in Python
Fonte: https://www.section.io/engineering-education/building-a-time-series-weather-forecasting-application-in-python/
Dados: https://www.kaggle.com/datasets/grubenm/austin-weather
"""

import pandas as pd
from neuralprophet import NeuralProphet
from matplotlib import pyplot as plt

# Importando e baixando os dados da url do drive
url='https://drive.google.com/file/d/1RZ1DX76zAA5GDKaQnaVFOB3KMoLiWxHh/view?usp=sharing'
file_id=url.split('/')[-2]
dwn_url='https://drive.google.com/uc?id=' + file_id

df = pd.read_csv(dwn_url) # Lê o arquivo e manda a tabela pra variavel
"""
# Visualizando a tabela
# Escrevi apenas pra ter uma colinha!

print(df.tail()) # Função que pega os ultimos elementos da tabela
print(df.Date.unique()) # Função que pega os valores unicos da coluna Date
print(df.columns) # Função que pega as colunas da tabela
print(df.dtypes) # Função que pega os tipos das colunas da tabela
print(df.shape) # Função que pega o tamanho da tabela
print(df.describe()) # Função que pega as descrições das colunas da tabela
print(df.info()) # Função que pega as informações das colunas da tabela
print(df.isnull().sum()) # Função que pega os valores nulos das colunas da tabela
print(df.isna().sum()) # Função que pega os valores nulos das colunas da tabela
print(df.head()) # Função que pega os primeiros elementos da tabela
"""

# Convertendo a coluna Date para o formato datetime
df['Date'] = pd.to_datetime(df['Date'])

# Plotando a tabela (data x temperatura)
plt.plot(df['Date'], df['TempAvgF'])
plt.show()

# Criando uma nova coluna
new_column = df[['Date', 'TempAvgF']]
new_column.dropna(inplace=True) # Função que remove os valores nulos da tabela
new_column.columns = ['ds', 'y'] # Renomeando as colunas
print(new_column.tail())

# Gerando um modelo de predição com o NeuralProphet

# Carregando o modelo
model = NeuralProphet()

# Treinando o modelo
model.fit(new_column, freq='D')

# Predição para daqui 1500 dias
future = model.make_future_dataframe(new_column, periods=1500)

# Gerando a predição
forecast = model.predict(future)
print(forecast.tail())

# Plotando a predição
plt.plot(forecast['ds'], forecast['yhat1'])
plt.show()
