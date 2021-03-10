import pandas as pd
df = pd.read_csv('data/dataset.csv')
df.head
df.shape

# Tipos de dados no dataframe


# Manipulando dataframe

# Selecionando colunas
df['Idade']
df[['Idade', 'Escolaridade']]

df.filter(like = 'p')

# Selecionando linhas
df.loc[4:6, ]
df.loc[[0, 4, 7], ]

df[df.Idade > 3]
df[df.Genero == 'Homem']

df[(df.Genero == 'Homem') & (df.Idade > 4)]


# Selecionando linhas e colunas
df.loc[4:6, 'p1':'p6']
df.loc[4:6, ['Idade', 'Consumo']]

my_filter = df.isin({"Genero": ['Homem'], "Consumo": ['Sim']})
df[(my_filter.Genero) & (my_filter.Consumo)]


# Selecionando linhas e colunas (somente intervalos numericos)
df.iloc[[3, 8, 10], [2, 5, 6]]
df.iloc[[3, 8, 10], 0:3]

# Ordenacao
df.sort_values("Idade")
df.sort_values("Genero")
df.sort_values(["Idade", "Genero"])

df.sort_values("Idade", inplace=True) # modifica o dataframe

# Ordenacao inversa
df.sort_values("Idade", ascending=False)
df.sort_values(["Idade", "p1"], ascending=[False, True])

# Calcular somatório variaveis p
df.filter(like = 'p').sum(axis = 1)

# Funcoes descritivas
df.filter(like = 'p').sum(axis = 1).mean()

# Group by
profile_vars = ['Genero', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6']
df[profile_vars].groupby('Genero').mean()

profile_vars2 = ['Genero', 'Consumo', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6']
df[profile_vars2].groupby(['Genero', 'Consumo']).mean()


