# This project can be found at
# https://www.kaggle.com/leandrodoze/sentiment-analysis-in-portuguese/notebook

# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python

# Análise de sentimento de Tweets de Minas Gerais

# --- Importando as bibliotecas --- #
import pandas as pd
from sklearn import metrics
from sklearn.model_selection import cross_val_predict
from sklearn.feature_extraction.text import CountVectorizer

# --- Carregamento de dados --- #
url='https://drive.google.com/file/d/1Ds6zhEE7HJgLPP22ZVDVmkWjODr_jxFc/view?usp=sharing'
file_id=url.split('/')[-2]
dwn_url='https://drive.google.com/uc?id=' + file_id

# Download dos dados do kaggle
dataset = pd.read_csv(dwn_url)

# --- Verificando os dados --- #
"""
# Mostrar linhas inicias da tabela
print(dataset.head())
print()
# Quantidade de dados
print(dataset.count())
print()
# Os classificados como neutro
print(dataset[dataset.Classificacao == 'Neutro'].count())
print()
# Os classificados como positivo
print(dataset[dataset.Classificacao == 'Positivo'].count())
print()
# E os classificados como negativo
print(dataset[dataset.Classificacao == 'Negativo'].count())
print()
"""
# --- Separando os dados --- #

# Próximo passo, vamos separar os tweets e suas classes
tweets = dataset["Text"].values
print(tweets)
print()
classes = dataset["Classificacao"].values
print(classes)
print()

# Vamos usar algumas frases de teste para fazer a classificação com o modelo treinado
testes = ["Esse governo está no início, vamos ver o que vai dar",
          "Estou muito feliz com o governo de São Paulo esse ano",
          "O estado de Minas Gerais decretou calamidade financeira!!!",
          "A segurança desse país está deixando a desejar",
          "O governador de Minas é do PT",
          "O prefeito de São Paulo está fazendo um ótimo trabalho"]

# --- Preparação do modelo --- #

# Random Forest
from sklearn.ensemble import RandomForestClassifier
forest = RandomForestClassifier(n_estimators=100)

# --- Treinamento do modelo --- #

# Inicializar o bag of words com um parâmetro máximo de features
vectorizer = CountVectorizer(analyzer = "word", tokenizer = None, preprocessor = None,
                             stop_words = None, max_features = 5000)
# Treinar o modelo, aprender o vocabulário e transformar nossos dados de treinamento em feature vectors
train_data_features = vectorizer.fit_transform(tweets)
# Ajusta a forest ao dataset de treinamento usando a bag of words como feature e os sentimentos
# como a resposta variável
forest = forest.fit(train_data_features, classes)

# --- Avaliação do modelo --- #

resultados = cross_val_predict(forest, train_data_features, classes, cv = 10)
# Medidas de validação do modelo
sentimentos = ['Neutro', 'Positivo', 'Negativo']
print(metrics.classification_report(classes, resultados, target_names = sentimentos))

# --- Classificação de tweets --- #

# Criar a BOW de teste
test_data_features = vectorizer.transform(testes)
# Fazendo a predição
resultados = forest.predict(test_data_features)
# Disposição de dados em tabela
testes_id = [1, 2, 3, 4, 5, 6]

data_frame = pd.DataFrame(data = { "id": testes_id, "texto": testes, "sentimento": resultados })
print(data_frame)

# Está bem ruim, vamos melhorar o modelo
