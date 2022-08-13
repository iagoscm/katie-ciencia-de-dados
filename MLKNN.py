from sklearn.model_selection import train_test_split # Modulo de divisão dos dados
from sklearn.metrics import accuracy_score, confusion_matrix # Modulo para avaliação
from sklearn import  datasets # Dados do dataset Iris
from sklearn import neighbors # Modulo do modelo KNN
from sklearn import tree # Modulo do modelo Arvore de Decisao

# Classificação; aprendizado supervisionado

iris = datasets.load_iris() # Carrega o data_set das iris na variavel

x = iris.data # Dados de entrada
y = iris.target # Dados esperados

# Divisão de dados para treinamento e teste, tendo a proporção de 70/30
input_treino, input_teste, output_treino, output_teste = train_test_split(x,y,test_size=.3)

# Definição do modelo KNN
classificador_knn = neighbors.KNeighborsClassifier()

# Definição do modelo de Árvore de Decisão
classificador_arvore = tree.DecisionTreeClassifier()

# Treinando os modelos
classificador_knn.fit(input_treino, output_treino)
classificador_arvore.fit(input_treino, output_treino)

# Fazendo predições usando os dados de entrada
knn_predicoes = classificador_knn.predict(input_teste)
arvore_predicoes = classificador_arvore.predict(input_teste)

# Avaliando as predições de cada modelo
print(accuracy_score(output_teste, knn_predicoes))      # geralmente tem a acuracia maior, entre 94-97%
print(accuracy_score(output_teste, arvore_predicoes))   # geralmente tem a acuracia menor, entre 86-92%

# OBS.: Tive que fazer um ajuste no `stats` do `scipy`, trocando
# o keepdims da função mode de None para True, em ordem de um
# desaparecimento de um warning
