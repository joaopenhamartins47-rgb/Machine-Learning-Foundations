#Analisando 1 cliente
#Se o cliente eh bom, ok ou ruim em nota de credito (score de credito)

#Passo a passo
#Passo 1: Importar a base de dados
#Passo 2: Tratar e preparar a base de dados para a inteligencia artificial
#Passo 3: Criar o modelo de previsao -> Ruim, Ok, Boa
#Passo 4: Avaliar e escolher o melhor modelo

import pandas as pd

df = pd.read_csv("clientes.csv")

# Passo 2:
# LabelEncoder para transformar variaveis string em formato texto para poder treinar os dados

#Profissao
#mix_credito
#comportamento_pagamento

from sklearn.preprocessing import LabelEncoder
cod_profissao = LabelEncoder()
df["profissao"] = cod_profissao.fit_transform(df["profissao"])

cod_mix_credito = LabelEncoder()
df["mix_credito"] = cod_mix_credito.fit_transform(df["mix_credito"])

cod_comportamento_pagamento = LabelEncoder()
df["comportamento_pagamento"] = cod_comportamento_pagamento.fit_transform(df["comportamento_pagamento"])

#A unica variavel que pode ser texto eh a que vamos prever, o resto transforma em numero

