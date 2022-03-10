import pandas as pd
import requests, json
import numpy as np
from numpy import percentile
import matplotlib.pyplot as plt
import csv
import seaborn as sns
from openpyxl import Workbook

data = pd.read_csv('Pokemon.csv')
# print(data)

# name = data['Name']
# type1 = data['Type 1']
# print(name)

# test = data.groupby('Name')[['Legendary']].head()
# print(test)

# medelvärde
# Total,HP,Attack,Defense,Sp. Atk,Sp. Def,Speed
# attack_mean = data['Attack'].head() -.mean()

# Attack = 'Attack'

# def spec_pok(Attack):
#     if Attack >= 80:
#         return 'Good'
#     elif Attack == 50:
#         return 'cool'
#     else:
#         return 'trash bro'

# visar en graf med alla stats
# data.plot(title='Pokemon attack', kind='line')
# plt.ylabel('#') # label = namnet på axeln
# plt.xlabel('Attack')
# plt.show()

# visar graf på generationernas attack stat
# fig, scat = plt.subplots(figsize=(10, 6))
# scat.scatter(data['Generation'], data['Attack'])
# scat.set_xlabel('Generation')
# scat.set_ylabel('Attack')
# plt.show()

# bäst resultat med scatter för vårat dataset. histogram kan bli missvisande med vårat dataset.
# fig, scat = plt.subplots(figsize=(10, 6))
# scat.scatter(data['Generation'], data['Attack'])
# scat.set_xlabel('Generation')
# scat.set_ylabel('Attack')
# plt.show()

# sorterar efter ex hp, namn... (lägst till högst, a - z)
# visar endast angivna
# ta bort values så visas allt
# dataTable = pd.pivot_table(data, index=["Name"], values=["HP"])
# print(dataTable)

# konverterar csv till excel / skapar tabell
wb = Workbook()
ws = wb.active
with open('Pokemon.csv', 'r') as f:
    for row in csv.reader(f):
        ws.append(row)
wb.save('Pokemon.xlsx')