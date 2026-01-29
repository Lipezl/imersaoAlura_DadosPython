import pandas as pd
import numpy as np
df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

# Verificar valores nulos no DataFrame
print(df.isnull())

# Contar valores nulos por coluna
print(df.isnull().sum())
print(df['work_year'].unique())

# Exibir linhas com valores nulos
print(df[df.isnull().any(axis=1)])

#Preencher valores nulos com a média da coluna
df_salarios = pd.DataFrame({
    'nome': ["Felipe", "Ana", "João", "Maria", "Pedro"],
    'salario': [np.nan, 6000, np.nan, 8000, 20000]
})

df_salarios['salario_media'] = df_salarios['salario'].fillna(df_salarios['salario'].mean().round(2)) # mean -> media // round(2) -> arredondar para 2 casas decimais
df_salarios['salario_mediana'] = df_salarios['salario'].fillna(df_salarios['salario'].median().round(2)) # median -> mediana // round(2) -> arredondar para 2 casas decimais

print(df_salarios)

df_temperaturas = pd.DataFrame({
    "Dia": ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"],
    "Temperatura": [30, np.nan, np.nan, 28, 27]
})

# Preencher valores nulos com o valor anterior (forward fill)
df_temperaturas['Preenchido_ffill'] = df_temperaturas["Temperatura"].ffill()
print(df_temperaturas)

# Preencher valores nulos com o valor posterior (backward fill)
df_temperaturas['Preenchido_bfill'] = df_temperaturas["Temperatura"].bfill()
print(df_temperaturas)

# Preencher valores nulos com um valor específico
df_cidades = pd.DataFrame({
    'nome': ["Felipe", "Ana", "João", "Maria", "Pedro"],
    'cidade': ["São Paulo", np.nan, "Rio de Janeiro", np.nan, "Belo Horizonte"]
})

df_cidades['cidade_preenchida'] = df_cidades['cidade'].fillna("Não informado")
print(df_cidades)

# Remover linhas com valores nulos
df_limpo = df.dropna()
df_limpo.isnull().sum()
print(df_limpo.isnull().sum())

# Alterar o tipo de dado de uma coluna
df_limpo = df_limpo.assign(work_year=df_limpo['work_year'].astype('int64'))
print(df_limpo.head())