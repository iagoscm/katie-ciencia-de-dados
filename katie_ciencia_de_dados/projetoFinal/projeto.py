"""
Projeto final

Alexia Naara
Iago Campelo
"""

# Importação dos módulos
import pandas as pd
from matplotlib import pyplot as plt
import io

# Le o conteudo do arquivo
df = pd.read_csv('Students_data.csv')

# Tratamento de dados (retirando o desnecessario)
media = df.drop(columns=['class','GPA','ID','race','from1','from2','from3','from4','gender','y'])

# Isola os aprovados
aprovados = df['y']

# Faz a media dos alunos
tabela_medias = media.median('columns', True)

# Criando e ordenando a tabela
aprovados_table = {'aprovacoes': aprovados}
aprovados_table = pd.DataFrame(data = aprovados_table)
aprovados_table = aprovados_table.sort_values(by='aprovacoes')

# Plotando o grafico
plt.scatter(tabela_medias, aprovados_table)
plt.title("Media por tipo de aprovação")
plt.xlabel("Médias")
plt.ylabel("Tipo de aprovação")
plt.show()
