import numpy as np
import pandas as pd

# Get the important stuff from the dataframe
df = pd.read_csv("raw_student_grades.csv", sep=",", header=0)
df.drop(index=df.index[0], axis=0, inplace=True)
l = list(df) # This is a list of the headers of df
print('\n\tWhich test do you want to grade?\n')
for i in range(4, len(l)):
    print(f'{i}: {l[i]}')
p = int(input('\n\tI want to grade test number ')) # This is the index the user wants to grade
df = df[[l[2], l[p]]]
df.rename(columns={
    l[2]: 'login',
    l[p]: 'score'
    }, inplace=True)

df['score'] = df['score'].fillna(0)

# Now df is just two columns with the login (text before the @ in the mail) and the score of the test

df2 = pd.read_csv("all_students.csv", sep=",", header=0)
df2.rename(columns={'Email': 'login', 'Nombre Estudiante': 'name'}, inplace=True)
df2 = df2[['name', 'login']] # So df2 is the name and login given by labmat of the student
df2['login'] = df2['login'].apply(lambda x: x.split('@')[0]) # Get only the name and not the domain

df2 = pd.merge(df2, df, on='login', how='left')
df2.drop(columns=['login'], inplace=True)
df2['score'] = df2['score'].fillna(0)
df2.to_csv('students_grades.csv', index=False)
print('Done!')

