# Referência
# https://www.askpython.com/python-modules/gensim-word2vec

import string
from xml.dom.minidom import Document
import nltk # Módulo de PLN
from nltk.corpus import brown
from gensim.models import Word2Vec
from sklearn.decomposition import PCA
from matplotlib import pyplot

nltk.download("brown") # Baixar o corpus de Brown, um módulo de palavras (conjunto de dados)

# Preprocessando o corpus de Brown para minúsculas e removendo pontuações
document = brown.sents()
data = []
for sent in document:
    new_sent = []
    for word in sent:
        new_sent.append(word.lower())
    data.append(new_sent)

# Criando o modelo Word2Vec
model = Word2Vec(
    sentences = data, # corpus de Brown
    vector_size = 50, # tamanho do vetor de 50 dimensões
    window = 10, # tamanho da janela de 10 palavras
    epochs = 20, # número de iterações
    min_count = 1, # número mínimo de vezes que uma palavra aparece no corpus
    workers = 2 # número de processadores
)

# Vetor para a palavra "love"
print("Vetor para love:")
print(model.wv["love"])
print()

# Computando a similaridade entre duas palavras
print("Similaridade entre love e hate:")
print(model.wv.similarity("love", "hate"))
print()

# Procurando palavras similares à woman e king, e tirando o que relaciona à man
print(model.wv.most_similar(positive=['woman', 'king'], negative=['man'], topn=10))

# Procurando palavras mais similares
print("5 palavras similares à john")
words = model.wv.most_similar("john", topn=5)
for word in words:
    print(word)
print()

# Visualizando dados
words = ["france", "germany", "india", "truck", "boat", "road", "teacher", "student", "book", "tv",
         "president", "computer", "baseball", "football", "tree", "river"]
X = model.wv[words]
pca = PCA(n_components=2)
result = pca.fit_transform(X)
pyplot.scatter(result[:, 0], result[:, 1])
for i, word in enumerate(words):
    pyplot.annotate(word, xy=(result[i, 0], result[i, 1]))
pyplot.show()
