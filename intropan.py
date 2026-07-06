import pandas as pd

#Leitura
df_vendas = pd.read_csv("vendas_tech.csv", encoding='utf-8', sep=',', low_memory=False)
df_loja = pd.read_excel("gerentes_lojas.xlsx")


#Ler os 5 primeiros
print(df_vendas.head())

#Ler os 5 ultimos, pode-se colocar valores dentro do parametro para dizer quantos serao exibidos
print(df_vendas.tail())

#Pegar 5 amostras
print(df_vendas.sample())

#Saber o formato do teu arquivo (shape)
print(f'shape: {df_vendas.shape}')

#Saber as colunas
print(df_vendas.columns)

#Para limpeza de dados, saber as info e para dados estatisticos, podem ser uteis o info e o describe respectivamente
print(df_vendas.info())
print(df_vendas.describe())