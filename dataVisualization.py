import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

sns.set_style('whitegrid')

# Meu dataframe
df = pd.read_csv('https://raw.githubusercontent.com/EliasNsilva/Dados-curso-de-verao/main/death-rates-from-air-pollution.csv?token=GHSAT0AAAAAABVZQUDM2YYICMGMHT7WVDZUYXBKJPQ')

# Renomeando as colunas

df = df.rename(columns= {'Year': 'Ano',
                        'Entity': 'Pais',
                        'Air pollution (total) (deaths per 100,000)': 'Total_de_mortes',
                        'Indoor air pollution (deaths per 100,000)': 'Mortes_poluição_interna',
                        'Outdoor particulate matter (deaths per 100,000)':'Mortes_poluição_externa',
                        'Outdoor ozone pollution (deaths per 100,000)':'Mortes_por_ozonio'})

# Mostrar resumo estatístico do conjunto de dados
print(df.describe())

# Desconsiderando a coluna Ano dos dados
# df = df.drop(['Ano'], axis=1)
# print(df.describe())

# Descartando dados com valores nulos
df = df.dropna() # deu bastante problema usar drop com o inplace=True, não sei porque
print(df.describe())

# Plotando gráfico de linhas
plt.figure(figsize=(15,15))

sns.lineplot(data=df, x="Ano", y='Total_de_mortes')
sns.lineplot(data=df, x=df['Ano'], y=df['Mortes_poluição_interna'])
sns.lineplot(data=df, x=df['Ano'], y=df['Mortes_poluição_externa'])
sns.lineplot(data=df, x=df['Ano'], y=df['Mortes_por_ozonio'])

plt.title("Mortes anuais por poluição atmosférica (mundial)")
plt.legend(labels=['Total de mortes', 'Mortes poluição interna', 'Mortes poluição externa', 'Mortes por ozonio'])
plt.show()

# Plotando histograma
fig, axes = plt.subplots(2,2, figsize=(20,8))

sns.histplot(ax=axes[0,0], data=df, x='Total_de_mortes', bins=25)
sns.histplot(ax=axes[0,1], data=df, x='Mortes_poluição_externa', bins=25)
sns.histplot(ax=axes[1,0], data=df, x='Mortes_poluição_interna', bins=25)
sns.histplot(ax=axes[1,1], data=df, x='Mortes_por_ozonio', bins=25)

fig.suptitle("Distribuição dos dados")
plt.show()

# Criando um dataframe com os dados das médias por país.
df_gp = df.groupby('Pais', as_index=False).mean().sort_values('Total_de_mortes', ascending=False)
plt.figure(figsize=(18,10))
plt.xticks(rotation=45)
plt.show()

# Plotando gráfico de torta
plt.figure(figsize=(12,8))
plt.pie(df_gp['Total_de_mortes'][0:10], labels=df_gp['Pais'][0:10])
plt.title("Países com maior média de mortes")

plt.show()

# Isolando os dados de um país
df_brasil = df[df['Pais'] == 'Brazil']

# Plotando boxplot
plt.figure(figsize=(8,12))
sns.boxplot(y='Total_de_mortes', data=df_brasil)
plt.show()

# Plotando histograma
fig, axes = plt.subplots(figsize=(20,8))
sns.histplot(data=df_brasil, x='Total_de_mortes', bins=15)
fig.suptitle("Distribuição dos dados")
plt.show()

# Plotando gráfico de linhas
plt.figure(figsize=(12,8))
sns.lineplot(x='Ano', y='Total_de_mortes', data= df_brasil)
plt.title("Total de mortes no Brasil")
plt.show()

# Isolando um ano para fazer um gráfico com mapa
df_ano = df[df['Ano'] == 2010]
print(df_ano.head(10))

fig = px.choropleth(
    df_ano['Total_de_mortes'],
    locations=df_ano['Pais'],
    #color=df_ano['Total_de_mortes'],
    color=np.log10(df_ano['Total_de_mortes']),
    hover_data=['Total_de_mortes'],
    locationmode="country names"
)

fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(title_text="Total de mortes por poluição em 2010 Heat Map")
fig.update_coloraxes(colorbar_title="Mortes por poluição",colorscale="reds")
fig.show()
