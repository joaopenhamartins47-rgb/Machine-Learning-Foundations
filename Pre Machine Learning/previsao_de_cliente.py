#Analisando 1 cliente
#Se o cliente eh bom, ok ou ruim em nota de credito (score de credito)

#Passo a passo
#Passo 1: Importar a base de dados
#Passo 2: Tratar e preparar a base de dados para a inteligencia artificial
#Passo 3: Criar o modelo de previsao -> Ruim, Ok, Boa
#Passo 4: Avaliar e escolher o melhor modelo

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score


df = pd.read_csv("clientes.csv")

# Passo 2:
# LabelEncoder para transformar variaveis string em formato texto para poder treinar os dados

#Profissao
#mix_credito
#comportamento_pagamento


cod_profissao = LabelEncoder()
df["profissao"] = cod_profissao.fit_transform(df["profissao"])

cod_mix_credito = LabelEncoder()
df["mix_credito"] = cod_mix_credito.fit_transform(df["mix_credito"])

cod_comportamento_pagamento = LabelEncoder()
df["comportamento_pagamento"] = cod_comportamento_pagamento.fit_transform(df["comportamento_pagamento"])

#A unica variavel que pode ser texto eh a que vamos prever, o resto transforma em numero

# y eh quem eu vou prever (objetivo)
y = df["score_credito"]

# x eh quem eu vou usar para fazer a previsao (variaveis)
x = df.drop(columns=["score_credito", "id_cliente"])


x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3)

# Passo 3: Criar um modelo de previsao

# Importar o modelo
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

# Criar o modelo
modelo_arvore = RandomForestClassifier()
modelo_knn = KNeighborsClassifier()

# Treinar o modelo
modelo_arvore.fit(x_treino, y_treino)
modelo_knn.fit(x_treino, y_treino)

# Passo 4: Avaliar e escolher o melhor modelo

#Previsao
precisao_arvore = modelo_arvore.predict(x_teste)
precisao_knn = modelo_knn.predict(x_teste)

#Avaliacao
print(accuracy_score(y_teste, precisao_arvore))
print(accuracy_score(y_teste, precisao_knn))

# Como melhorar o modelo
# Gridsearch
# ter mais dados
# testar outros parametros

# Passo 5: Fazer novas previsoes

#Melhor modelo = Arvore de decisoes

#Importar novos clientes
novos_clientes = pd.read_csv("clientes.csv")

#Preparar os novos clientes
novos_clientes["profissao"] = cod_profissao.transform(novos_clientes["profissao"])
novos_clientes["mix_credito"] = cod_mix_credito.transform(novos_clientes["mix_credito"])
novos_clientes["comportamento_pagamento"] = cod_comportamento_pagamento.transform(novos_clientes["comportamento_pagamento"])
novos_clientes = novos_clientes.drop(columns=["score_credito", "id_cliente"])
previsao = modelo_arvore.predict(novos_clientes)

# Resumo:

# 1 - Transformar os dados categóricos (texto) em números para que o modelo consiga utilizá-los.
#
# 2 - Separar os dados em:
#    - X = variáveis de entrada (features)
#    - y = variável que quero prever (target)
#
# 3 - Dividir os dados em treino e teste usando:
#    train_test_split(X, y, test_size=0.3)
#
#    Resultado:
#    - x_treino
#    - x_teste
#    - y_treino
#    - y_teste
#
# 4 - Escolher um modelo (Random Forest, KNN, etc.) e treiná-lo com:
#    modelo.fit(x_treino, y_treino)
#
# 5 - Fazer previsões usando os dados de teste:
#    previsoes = modelo.predict(x_teste)
#
# 6 - Comparar as previsões com as respostas corretas usando uma métrica:
#    accuracy_score(y_teste, previsoes)
#
# 7 - Depois de escolher o melhor modelo, utilizá-lo para prever novos clientes,
#    aplicando exatamente o mesmo pré-processamento feito nos dados de treino.

