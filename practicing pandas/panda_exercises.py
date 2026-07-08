# Nível 1 — Aquecimento (exploração)

# 1 - Carregue cancelamentos.csv sem dropar CustomerID ainda. Mostre shape, dtypes e as 3 primeiras/últimas linhas.

import pandas as pd

df = pd.read_csv("../cancelamentos.csv")

print(df.shape)
print(df.head(3))
print(df.tail(3))

# 2 - Descubra quantos valores nulos existem por coluna (não é dropna() direto — é um metodo que conta nulos coluna a coluna).

print(df.info())

# 3 - Rode describe() só nas colunas idade e total_gasto (sem trazer as outras numéricas junto).

print(df[["idade", "total_gasto"]].describe())

# Nível 2 — Limpeza consciente

# 1 - Antes de rodar drop_duplicates(), descubra quantas linhas duplicadas existem

print(df.duplicated().sum())

# 2 -
