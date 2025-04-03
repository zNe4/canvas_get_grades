import numpy as np
import pandas as pd
import unicodedata


def clean_string(chain): # Removes accents
    return ''.join((c for c in unicodedata.normalize('NFD',chain) if unicodedata.category(c) != 'Mn'))


# Get exceptions
with open("last_name_exceptions.txt", "r", encoding='utf-8') as f:
    exceptions = {x.strip() for x in f.readlines()}

# Get the important stuff from the dataframe
df = pd.read_csv("raw_student_grades.csv", sep=",", header=0)
# print(df.head())
df.drop(df.columns[[i for i in range(1,98)]], axis=1, inplace=True)
df = df.sort_values(['name', 'score'], ascending=False).groupby('name').head(1)


# Remove accents
names = [
        clean_string(x)[::-1].split() for x in df['name'].to_list()
]

f_names = []
for name in names:
    t2 = name.pop(0) #Should be second name
    t1 = name.pop(0)
    if t1[::-1] in exceptions:
        t3 = name.pop(0)
        t1 = f'{t1} {t3}'
    name = name + [t2, t1]
    f_names.append(' '.join(name)[::-1])

# print(f_names[:5])
df.rename(columns={'name':'old_name'}, inplace=True)
# print(names[:5])
df.insert(loc=0, column='name', value=f_names)
# print(df.head())
df.drop("old_name", axis=1, inplace=True)
# print(df.head())
df.sort_values(by=['name'], inplace=True)
# print(df.head())

df2 = pd.read_csv("all_students.csv", sep=",", header=0)
df2.rename(columns={'Nombre Estudiante': 'name', 'Pregunta\nPTC1': 'score'}, inplace=True)
df2 = df2['name']

final = pd.DataFrame.merge(df, df2, how='outer', on='name', sort=True)
final.fillna(0, inplace = True)
final['score'] = final['score'].apply(lambda x: round(x, 2))
final.to_csv('students_grades.csv', index=False)
print('Done!')

