# Nível 1 — Aquecimento (exploração)

# 1 - Carregue cancelamentos.csv sem dropar CustomerID ainda. Mostre shape, dtypes e as 3 primeiras/últimas linhas.

import pandas as pd

df = pd.read_csv("../cancelamentos.csv")

# print(df.shape)
# print(df.head(3))
# print(df.tail(3))
#
# # 2 - Descubra quantos valores nulos existem por coluna.
#
# print(df.info())
#
# # 3 - Rode describe() só nas colunas idade e total_gasto (sem trazer as outras numéricas junto).
#
# print(df[["idade", "total_gasto"]].describe())
#
# # Nível 2 - Limpeza
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

# # Nível 3 - value_counts e primeiras comparações
#
# # 1 - Rode value_counts(normalize=True) para sexo, assinatura e duracao_contrato. Qual categoria tem mais representantes em cada uma?
#
# print(df['sexo'].value_counts(normalize=True))
# print(df['assinatura'].value_counts(normalize=True))
# print(df['duracao_contrato'].value_counts(normalize=True))
#
# # 2 - Problema real: qual a taxa de cancelamento (cancelou) separada por sexo?
#
# print(df.groupby('sexo')['cancelou'].mean())
#
# # 3 - Mesma pergunta, mas por duracao_contrato. Contratos mais longos cancelam menos? Confirme com números.
#
# print(df.groupby('duracao_contrato')['cancelou'].mean())

# Nível 4

# Compare a média de total_gasto entre quem cancelou e quem não cancelou. Cliente que cancela gasta mais ou menos, em média?

print(df.groupby('cancelou')['total_gasto'].median()) # -> Cliente que gasta mais tende a ter menores chances de cancelamento, utilizei median pois é menos influenciada por extremidades do que a média

# Faça o mesmo com ligacoes_callcenter. Existe alguma relação entre número de ligações pro call center e cancelamento?

print(df.groupby('cancelou')['ligacoes_callcenter'].mean())

# Crie faixas de idade usando pd.cut() (ex: 18-25, 26-35, 36-50, 51+) e calcule a taxa de cancelamento por faixa. Qual faixa etária cancela mais?

df['faixa_idade'] = pd.cut(df['idade'], bins=[18,25,35,45,55,65,100])
faixa = df.groupby('faixa_idade')['cancelou'].mean()
print(faixa)
print(faixa.map("{:.2%}".format))

