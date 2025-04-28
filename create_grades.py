import numpy as np
import pandas as pd
import unicodedata
from collections import defaultdict


def clean_string(chain): # Removes accents
    return ''.join((c for c in unicodedata.normalize('NFD',chain) if unicodedata.category(c) != 'Mn')).lower()


# Get the important stuff from the dataframe
df = pd.read_csv("raw_student_grades.csv", sep=",", header=0)
df.drop(index=df.index[0], axis=0, inplace=True)
# print(df.head())
l = list(df)
# print(l)
print('\n\tWhat test do you want to grade?\n')
for i in range(1, len(l)):
    print(f'{i}: {l[i]}')
p = int(input('\n\tI want to grade test number '))
df = df[[l[0], l[p]]]
df.rename(columns={
    l[0]: 'name',
    l[p]: 'score'
    }, inplace=True)

# df = df[['name', 'score']]
# p = input('\nDoes the test accept multiple attempts? [y/n] ')
# if p == 'y':
#     df = df.sort_values(['name', 'score'], ascending=False).groupby('name').head(1)
df['name'] = df.apply(lambda x: ''.join(x['name'].split('-')), axis=1)
df['name'] = df.apply(lambda x: ''.join(x['name'].split(',')), axis=1)
df['score'] = df['score'].fillna(0)
# print(df.head())


df2 = pd.read_csv("all_students.csv", sep=",", header=0)
df2.rename(columns={'Nombre Estudiante': 'name'}, inplace=True)
df2 = df2[['name']]

df2['name'] = df2.apply(lambda x: ''.join(x['name'].split('-')), axis=1)
names_array = [
        ' '.join(sorted(clean_string(x).split(' '))) for x in df['name'].tolist()
]
# Now each element in the array is the sorted name (unique) of a student.
scores_array= df['score'].tolist()

d = defaultdict(int)
for i in range(len(names_array)):
    d[names_array[i]] = round(scores_array[i], 2)

# And d is the dict containing the scores of the unique sorted name

df2['score'] = df2.apply(lambda x: d[' '.join(sorted(clean_string(x['name']).split(' ')))], axis=1)

df2.to_csv('students_grades.csv', index=False)
# print(df2.head())
print('Done!')

