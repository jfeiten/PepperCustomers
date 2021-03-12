# Learning pandas

# Dataset's variables

# Age
#   (1) younger than 18 years
#   (2) 18 - 26 years
#   (3) 27 - 35 years
#   (4) 36 - 44 years
#   (5) 45 - 53 years
#   (6) 54 - 62 years
#   (7) 63 - 71 years

# Education
#   1, 2: Primary
#   3, 4: Secondary
#   5, 6, 7: Tertiary

# Income
#   From 0 to R$1.254,00
#   From R$1.255,00 to R$2.004,00
#   From R$2.005,00 to R$8.640,00
#   From R$8.641,00 to R$11.261,00
#   R$11.262,00 or more

# Load modules
import pandas as pd

# Load dataset
df = pd.read_csv('data/dataset.csv')
df.head
df.shape
df

# Renaming variables
new_columns_name = ['Age', 'Education', 'Income', 'Sex', 'Profile',
                    'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'Consumption']

df.columns = new_columns_name
df

# Changing levels
df['Sex'] = df['Sex'].replace('Homem', 'Man')
df['Sex'] = df['Sex'].replace('Mulher', 'Woman')

df['Consumption'] = df['Consumption'].replace(['Sim', 'Não'], ['Yes', 'No'])
df

# Exporting dataset
df.to_pickle("data/df.pkl")

# Selecting columns
df['Age']
df[['Age', 'Education']]

df.filter(like = 'p')

# Selecting rows
df.loc[4:6, ]
df.loc[[0, 4, 7], ]

df[df.Age > 3]
df[df.Sex == 'Man']

df[(df.Sex == 'Man') & (df.Age > 4)]


# Selecting rows and columns
df.loc[4:6, 'p1':'p6']
df.loc[4:6, ['Age', 'Consumption']]

my_filter = df.isin({"Sex": ['Man'], "Consumption": ['Yes']})
df[(my_filter.Sex) & (my_filter.Consumption)]


# Selecting rows and columns (only numbers)
df.iloc[[3, 8, 10], [2, 5, 6]]
df.iloc[[3, 8, 10], 0:3]

# Ordering
df.sort_values("Age")
df.sort_values("Sex")
df.sort_values(["Age", "Sex"])

df.sort_values("Age", inplace=True) # changes the dataframe

# Descending ordering
df.sort_values("Age", ascending=False)
df.sort_values(["Age", "p1"], ascending=[False, True])

# Summing by rows
df.filter(like = 'p').sum(axis = 1)

# Summary functions
df.filter(like = 'p').sum(axis = 1).mean()

# Group by
profile_vars = ['Sex', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6']
df[profile_vars].groupby('Sex').mean()

profile_vars2 = ['Sex', 'Consumption', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6']
df[profile_vars2].groupby(['Sex', 'Consumption']).mean()

