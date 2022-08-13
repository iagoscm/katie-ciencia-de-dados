# Aulas e Conteúdos

![Cronograma](images/cronograma.png)

### Anotações sobre o conteúdo

<details>
<summary>Intro à Ciência de Dados + Python para Ciência de Dados</summary>

# Currículo de um Cientista de Dados
- Geralmente um profissional multidisciplinar, podendo vir de diversas áreas
- Possui conhecimentos em:
    - R, Python e SQL (Linguagens de análise e extração de dados)
    - Estatística e AI/Machine Learning
    - Tableu, PowerBI, streamlit, etc… (Tecnologia de visualização de dados e criação de relatórios)
    - Negócios e produtos

# Mercado de Trabalho
- Setor de varejo/saúde/financeiro/marketing
    - 9 posição em alta em 2022
    - 60 mil vagas não ocupadas em 2021
    - Média salárial de 6k-9k

# Intro a Ciência de Dados

- Combinação de cic, estat e mat que pode ser usada interdisciplinarmente
- Processo de extrair info através de dados
- Identificar tendências
- Dados → Análise → Decisão → Ação
    - O que aconteceu?
    - Por que aconteceu?
    - Acontecerá novamente?
    - O que deve ser feito?


![Competencias](images/competencias.png)

# Tipos de Modelo
- Descrição de fenômenos do mundo real e digital
- Geração de valor a negócios
- Automatizar processos para operações de:
    - Inferência/Predição
    - Classificação
    - Agrupamento
    - Recomendação
    # Modelos de Classificação
      - Modelo supervisionado, rotulado manualmente
    # Modelos de Agrupamento/Clusterização
      - Enviar um conjunto de características para a máquina para ela atribuir à um modelo específico
        - Agrupa bancos de dados com características comuns
        - Eu, como humano, posso rotular esses grupos que são agrupados
    # Modelos de Recomendação
      - Modelo colaborativo → Renner, Netflix, Amazon
      - Modelo pessoal → Netflix, Instagram, Tiktok

# Etapas de Geração de um Modelo
![Divisão de Dados](images/divisao_dados.png)

- Entrada de Dados
  - Separados entre treinamento e teste, um com ajuda humana e outro para testar a capacidade da máquina
- Coleta/Organização
  - Dados podem vir de múltiplas fontes
  - Tipicamente desorganizados
  - A combinação de múltiplas fontes de dados tem como objetivo criar modelos mais acurados
- Tratamento
    - Descarte
        - Dados em brancco
        - Dados de má qualidade
        - Anomalias
    - Preenchimento de dados faltantes
        - Interpolação
        - Substituição por valores de média, moda ou mediana
    - Transformação
        - Normalização
        - Codificação
        - Engenharia de características
- Concepção do modelo
  - Separação da base de dados entre teste e treinamento
      - No treinamento a gente dá o rótulo das características, ou seja, o resultado com base na entrada
  - Escolha do modelo conforme a aplicação:
      - Classificação ou Predição
          - KNN
          - ARIMA
          - Long-Short Term Memory
          - Neural networks
          - …
      - Agrupamento
          - K-means
          - Mean-shift clustering
          - DBSCAN
          - Gaussian Mixture Models
          - …
      - Recomendação
          - Collaborative filtering
          - Content-based filtering
- Avaliação dos resultados
- Validação
    - Teste
        - Teste de hipótese (análise do p-valor) e confirmação de tese
        - Validação cruzada
        - Análise de métricas de avaliação
            - Acurácia, precisão, erro médio absoluto
    - Aprovação do resultado por gestores e clientes
- Implantação
      - Lançamento do modelo em produção
      - Geração de valor ao negócio
      - Monitoramento e aprimoramento contínuo do modelo
</details>

<details>
<summary>Inteligência Artificial e Aprendizado de Máquina + Introdução ao Python para Ciência de Dados</summary>

# Introdução à Inteligência Artificial

## Dividido em 4 definições:
- Pensamento humanizado

    > O fascinante esforço de fazer computadores pensar… Máquinas com mentes, no completo sentido literal. (Haugeland, 1985)
    >

    > A automação de atividades que associamos com pensamento humano, atividades como tomada de decisão, resolução de problema, aprendizado… (Bellman, 1978)
    >
- Pensamento racional

    > É o estudo das faculdades mentais através de modelos computacionais (Charniak e McDermott, 1985)
    >

    > É o estudo da computação que torna possível sentir, racionalizar, e agir. (Winston, 1992)
    >
- Agir humanamente

    > É a arte de construir máquinas que executam funções que demandam
    inteligência, quando executadas por pessoas. (Kurzweil, 1990)
    >

    > É o estudo de como fazer computadores realizarem coisas que, no
    momento, as pessoas fazem de maneira melhor. (Rich and Knight, 1991)
    >
- Agir racionalmente

    > Inteligência computacional é o estudo da criação de agentes
    inteligentes.” (Poole et al., 1998)
    >

    > IA se preocupa com comportamento inteligente em artefatos. (Nilsson, 1998)


# Teste de Turing
- Agir humanamente da máquina
- Um computador é aprovado no teste de Turing se um humano, após fazer uma série de perguntas, não sabe distinguir se as respostas são de uma máquina ou de outro humano.
- Para uma máquina passar nesse teste, demandaria:
    - Processamento de linguagem natural, ou seja, se comunicar em algum idioma
    - Representação de conhecimento, ou seja, armazenar o que vê e ouve
    - Raciocínio automático, ou seja, usar o conhecimento armazenado para responder perguntas e chegar à conclusões
    - Aprendizado de máquina, que é adaptar-se à novas circunstâncias, identificar padrões e fazer generalizações
# Atlas <3
- Boston Dynamics
- Área da robótica
- OBS.: Me lembra muito minha vontade de trabalhar com robótica, reabilitação, exoesqueletos e impulsos elétricos
# Dall-E
- Rede neural que reproduz imagens por instruções de texto
# Aprendizado de Máquina
- Sub-área do campo da inteligência artificial
- Capacidade da máquina de imitar o comportamento inteligente humano
- Divide-se em:
    - Aprendizado supervisionado (dados rotulados)
    - Aprendizado não-supervisionado (dados não-rotulados)
    - Aprendizado por reforço (tentativa e erro)

# Métricas de avaliação
- Matriz de confusão
![Matriz de Confusão](images/matriz_de_confusao.png)

- Métricas de avaliação de classificação
![Métricas Classificação](images/metricas_avaliacao.png)

- Diferença entre acurácia e precisão
    - O modelo acurado geralmente acerta o alvo, enquanto o preciso é ter consistência nos resultados
![Exemplos Acurácia e Precisão](images/exemplos_acuracia_precisao.png)

- Viés e Variância
    - É preferível que sejam baixos para que sejam resultados acurados e com pouco erro mínimo
![Modelos Viés e Variância](images/modelos_vies_variancia.png)

  - Nesse gráfico, é possível enxergar a relação entre viés e variância
![Graficos Viés e Variância](images/grafico_vies_variancia.png)

# Análise de Regressão
  - Objetiva gerar modelos matemáticos ajustados a um conjunto de dados
  - O modelo define e prevê padrões no conjunto de dados
  - O melhor modelo é definido de acordo com uma função de erro, a qual deve ser minimizada
  - Tipos comuns de modelos regressivos:
      - Linear
      - Polinomial
      - Logístico (Classificação Binária)
![Graficos Modelos Regressivos](images/graficos_modelos_regressivos.png)

# Modelo de regressão: avaliação de erro
- Funções comuns:
  - Erro médio absoluto (MAE)
  - Erro quadrático médio (MSE)
  - Raiz do erro quadrático médio (RMSE)
  - Erro percentual absoluto médio (MAPE)

# Processamento de Linguagem Natural
- Leitura, processamento e análise de escrita humana (linguagem natural) em idiomas como português, inglês, francês.
- Onde se aplica?
  -  Análise de sentimentos;
  -  Conversão automática de voz para texto ou vice-versa;
  -  Modelos de conversação;
  -  Gerador de texto
     -  Jornais;
     -  Artigos científicos;
     -  Livros de ficção.
- Artigo escrito pela própria IA para se descrever:
  > Can GPT3 write an academic paper on itself, with minimal human input?
  > https://hal.archives-ouvertes.fr/hal-03701250/document
![Cerebro com Várias Palavras](images/procLingNeural.png)


# Similaridade Semântica: Paragraph2Vec
- É um modelo de representação de texto que utiliza a similaridade semântica entre frases para gerar um vetor de dimensão fixa.
- Modelo Distributed Memory (DM): Uso de palavras do contexto para inferir uma palavra.
- Modelo Distributed Bag of Words (DBOW): Inferência de um conjunto de palavras associadas ao contexto de uma palavra de entrada.

# Reconhecimento de Entidades Nomeadas (NER)
- Treinamento de um modelo para reconhecer entidades nomeadas em um texto
- Modelos podem ser treinados: ("Dia 15/11/2021 será feriado", {'entities': [(4,14)], ['DATE']})
- Alguns pacotes disponibilizam modelos: NLTK, SpaCy, Stanford NER.
- Supervisionado

# Bibliotecas para PLN
- Word2Vec;
- Paragraph2Vec;
- FastText;
- SpaCy;
- SBERT;

# Redes Neurais Artificiais
- Redes Neurais Artificiais (R.N.A.) são redes neurais que utilizam a tecnologia de computação para aprender a reconhecer padrões em um conjunto de dados.
- RNAs são inspiradas no cérebro humano, que é capaz de aprender a reconhecer padrões em um conjunto de dados.
- Sua estrutura contém:
  - Neurônios;
  - Camadas:
    - Entrada;
    - Intermediárias;
    - Saída;
  - Sinapses (links|conexões) entre os neurônios;
  - Função de ativação;
  - Peso da sinapse (p).
- RNAs com mais de 3 camadas, incluindo a camada entrada e saída, são chamadas de redes profundas, modelos de aprendizagem profunda.
![Funcionamento do neurônio](images/neuronio.png)
- As camadas entre entrada e saída são chamadas de camadas ocultas.
- Tipos e aplicações
  - Rede Neural Recurrente (R.N.R.| R.N.N. em inglês)
    - ideal para séries temporais e predições (vendas, mercado, tempo).
  - Rede Neural Convolucional (R.N.C.| C.N.N. em inglês)
    - ideal para identificar padrões, reconhecimento de imagens e visão computacional.
  -

# A Rede Neural Perceptron
- É um modelo de aprendizado supervisionado para classificação binária;
- É uma rede neural cujos os pesos e inclinações podem ser treinados para produzir um vetor alvo que quando apresentamos tem que corresponder ao vetor de entrada.
- Criada em 1958 por Frank Rosenblatt;
- Modelo mais antigo;
- Composta por:
  - Uma entrada;
  - Uma saída;
  - Um neurônio.


</details>
