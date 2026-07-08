# import pandas as pd
#
# #Leitura
# df_vendas = pd.read_csv("vendas_tech.csv", encoding='utf-8', sep=',', low_memory=False)
# df_loja = pd.read_excel("gerentes_lojas.xlsx")
#
#
# #Ler os 5 primeiros
# print(df_vendas.head())
#
# #Ler os 5 ultimos, pode-se colocar valores dentro do parametro para dizer quantos serao exibidos
# print(df_vendas.tail())
#
# #Pegar 5 amostras
# print(df_vendas.sample())
#
# #Saber o formato do teu arquivo (shape)
# print(f'shape: {df_vendas.shape}')
#
# #Saber as colunas
# print(df_vendas.columns)
#
# #Para limpeza de dados, saber as info e para dados estatisticos, podem ser uteis o info e o describe respectivamente
# print(df_vendas.info())
# print(df_vendas.describe())
# print(df_vendas.drop(columns='nome_coluna')
#==================================================================================

#Projeto analise de dados
import pandas as pd

df = pd.read_csv("../cancelamentos.csv")

#Tirar uma coluna
df = df.drop(columns="CustomerID")
print(df.info())

#Excluir valores vazios
df = df.dropna()
#Exclui informacoes duplicadas
df = df.drop_duplicates()
print(df.info())

#Quantos clientes cancelaram, contar quantos sao 1 na coluna cancelou
print(df["cancelou"].value_counts())
print(df["duracao_contrato"].value_counts(normalize=True).map("{:.2%}".format))

#Porcentagem
print(df["cancelou"].value_counts(normalize=True).map("{:.1%}".format))

import plotly.express as px

for coluna in df.columns:
    #Criar o grafico
    grafico = px.histogram(df, x=coluna, color="cancelou")
    #Mostrar o grafico
    grafico.show()

#Filtragem dos dados
condicao = df["duracao_contrato"] != "Monthly"
df = df[condicao]

condicao = df["ligacoes_callcenter"] <= 4
df = df[condicao]

df = df[df["dias_atraso"] <= 20]


print((df["cancelou"].value_counts(normalize=True).map("{:.1%}".format)))