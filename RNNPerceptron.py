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
