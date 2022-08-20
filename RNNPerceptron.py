# Fonte: https://python-course.eu/machine-learning/neural-networks-with-scikit.php

# --- Importando bibliotecas --- #
import matplotlib.pyplot as plt # Módulo para visualização de dados
from sklearn.datasets import make_blobs # Gerador de clusters (grupos)
from sklearn.model_selection import train_test_split # Separador de dados
from sklearn.neural_network import MLPClassifier # Modelo de rede neural (Multi Layer Perceptron)
from sklearn.metrics import accuracy_score # Métrica de avaliação

# --- Gerando dados --- #
n_amostras = 1000 # Número de amostras
centro_bolha = ([1,1], [3,4], [1,3.3], [3.5, 1.8]) # Centro de cada bolha

# Dados e rótulos
data, rotulos = make_blobs(n_samples=n_amostras,
  centers=centro_bolha,
  cluster_std=0.5,
  random_state=0
)

# Criando uma função para mostrar os dados

def mostrar_dados(data, rotulos):

  colours = ['red', 'green', 'blue', 'magenta'] # Cores para os grupos
  fig, ax = plt.subplots() # Criando figura e subplot

  for n_classes in range(len(centro_bolha)):
    x = data[rotulos == n_classes][:, 0] # Dados do eixo x
    y = data[rotulos == n_classes][:, 1] # Dados do eixo y
    cor = colours[n_classes] # Cor da bolha
    ax.scatter(x, y, c=cor, s=50, label=str(n_classes)) # Plotando os dados
  ax.legend() # Mostrando os rótulos
  plt.show() # Mostrando a figura

# --- Mostrando os dados --- #
mostrar_dados(data, rotulos)

# --- Separando dados para treinamento e teste --- #
dados_treinamento, dados_teste, rotulo_treinamento, rotulo_teste = train_test_split(data, rotulos, test_size=0.2)

# --- Criando o modelo de rede neural e o treinando --- #

# Rede Neural MLP com 1 camada oculta de 6 neurônios
clf = MLPClassifier(solver='lbfgs',
                    alpha=1e-5,
                    hidden_layer_sizes=(6,),
                    random_state=1,
                    max_iter=1000)

clf.fit(dados_treinamento, rotulo_treinamento)

# --- Testando o modelo --- #

predicoes_teste = clf.predict(dados_teste)
avaliacao = accuracy_score(predicoes_teste, rotulo_teste)
print("Resultado da avaliação nos dados de teste: ", avaliacao)
print(predicoes_teste[:20])
print(dados_teste[:20])
