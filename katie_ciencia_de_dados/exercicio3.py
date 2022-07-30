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
df.tail() # Função que printa os ultimos elementos da tabela
