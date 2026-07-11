# Nível 1 — Aquecimento (exploração)

# 1 - Carregue cancelamentos.csv sem dropar CustomerID ainda. Mostre shape, dtypes e as 3 primeiras/últimas linhas.

import pandas as pd

df = pd.read_csv("../cancelamentos.csv")

# print(df.shape)
# print(df.head(3))
# print(df.tail(3))
#
# # 2 - Descubra quantos valores nulos existem por coluna (não é dropna() direto — é um metodo que conta nulos coluna a coluna).
#
# print(df.info())
#
# # 3 - Rode describe() só nas colunas idade e total_gasto (sem trazer as outras numéricas junto).
#
# print(df[["idade", "total_gasto"]].describe())
#
# # Nível 2 — Limpeza consciente
#
# # 1 - Antes de rodar drop_duplicates(), descubra quantas linhas duplicadas existem
#
# print(df.duplicated().sum())
#
# # 2 - Faça o pipeline de limpeza completo (drop CustomerID → dropna → drop_duplicates) e imprima o shape antes e depois de cada etapa, pra você enxergar quanto cada uma "custou" em linhas perdidas.
#
# print(df.shape)
# # df = (
# #     df
# #     .dropna()
# #     .drop(columns="CustomerID")
# #     .drop_duplicates()
# # )
# df = df.dropna()
# df = df.drop(columns="CustomerID")
# df = df.drop_duplicates()
#
# print(df.shape)

# Nível 3 — value_counts e primeiras comparações

# 1 - Rode value_counts(normalize=True) para sexo, assinatura e duracao_contrato. Qual categoria tem mais representantes em cada uma?

print(df['sexo'].value_counts(normalize=True))
print(df['assinatura'].value_counts(normalize=True))
print(df['duracao_contrato'].value_counts(normalize=True))

# 2 - Problema real: qual a taxa de cancelamento (cancelou) separada por sexo?

print(df.groupby('sexo')['cancelou'].mean())
