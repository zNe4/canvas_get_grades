import numpy as np
import pandas as pd
import unicodedata
from collections import defaultdict


def clean_string(chain): # Removes accents
    return ''.join((c for c in unicodedata.normalize('NFD',chain) if unicodedata.category(c) != 'Mn')).lower()


# Get exceptions
with open("last_name_exceptions.txt", "r", encoding='utf-8') as f:
    exceptions = {x.strip() for x in f.readlines()}

# Get the important stuff from the dataframe
df = pd.read_csv("raw_student_grades.csv", sep=",", header=0)
# print(df.head())
df = df[['name', 'score']]
df = df.sort_values(['name', 'score'], ascending=False).groupby('name').head(1)
df['name'] = df.apply(lambda x: ''.join(x['name'].split('-')), axis=1)


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

# And d is the dict containig the scores of the unique sorted name

df2['score'] = df2.apply(lambda x: d[' '.join(sorted(clean_string(x['name']).split(' ')))], axis=1)

df2.to_csv('students_grades.csv', index=False)
print('Done!')

