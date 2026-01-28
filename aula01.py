import pandas as pd

#df -> dataframe
df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

# Exibir as primeiras linhas do DataFrame
print(df.head(10))

# Exibir informações sobre o DataFrame
print("\nInformações do DataFrame:")
print(df.info())

# Exibir a descrição estatística do DataFrame
print("\nDescrição Estatística do DataFrame:")
print(df.describe())

# Exibir o número de linhas e colunas do DataFrame
print("\nDimensões do DataFrame:")
print(df.shape)

# Exibir os nomes das colunas do DataFrame
print("\nNomes das Colunas:")
print(df.columns)

renomearColunas = {
    "work_year": "ano",
    "experience_level": "nivel_experiencia",
    "employment_type": "tipo_emprego",
    "job_title": "titulo_trabalho",
    "salary": "salario",
    "salary_currency": "moeda_salario",
    "salary_in_usd": "salario_usd",
    "employee_residence": "residencia_funcionario",
    "remote_ratio": "percentual_remoto",
    "company_location": "localizacao_empresa",
    "company_size": "tamanho_empresa"
}

df = df.rename(columns=renomearColunas)
print("\nNomes das Colunas após renomeação:")
print(df.columns)

# Contar valores únicos na coluna
df["nivel_experiencia"].value_counts()
print("\nContagem de Níveis de Experiência:")
print(df["nivel_experiencia"].value_counts())

df["tipo_emprego"].value_counts()
print("\nContagem de Tipos de Emprego:")
print(df["tipo_emprego"].value_counts())

df["percentual_remoto"].value_counts()
print("\nContagem de Percentuais Remotos:")
print(df["percentual_remoto"].value_counts())

df["titulo_trabalho"].value_counts()
print("\nContagem de Títulos de Trabalho:")
print(df["titulo_trabalho"].value_counts())

df["salario"].value_counts()
print("\nContagem de Salários:")
print(df["salario"].value_counts())

df["residencia_funcionario"].value_counts()
print("\nContagem de Residências dos Funcionários:")
print(df["residencia_funcionario"].value_counts())

df["localizacao_empresa"].value_counts()
print("\nContagem de Localizações das Empresas:")
print(df["localizacao_empresa"].value_counts())

df["tamanho_empresa"].value_counts()
print("\nContagem de Tamanhos das Empresas:")
print(df["tamanho_empresa"].value_counts())

renomearNiveis = {
    "EN": "Junior",
    "EX": "Executivo",
    "MI": "Pleno",
    "SE": "Sênior"
}
df["nivel_experiencia"] = df["nivel_experiencia"].replace(renomearNiveis)
print("\nNíveis de Experiência após renomeação:")
print(df["nivel_experiencia"].value_counts())

contrato = {
    "FT": "Tempo Integral",
    "PT": "Meio Período",
    "CT": "Contrato",
    "FL": "Freelancer"
}
df["tipo_emprego"] = df["tipo_emprego"].replace(contrato)
print("\nTipos de Emprego após renomeação:")
print(df["tipo_emprego"].value_counts())
remoto = {
    0: "Presencial",
    50: "Híbrido",
    100: "Remoto"
}
df["percentual_remoto"] = df["percentual_remoto"].replace(remoto)
print("\nPercentuais Remotos após renomeação:")
print(df["percentual_remoto"].value_counts())

print("\nDataFrame após todas as renomeações:")
print(df.head(10))

print(df.describe(include="object"))