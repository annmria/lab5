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
# attack_mean = data['Attack'].tail().mean()
# print (attack_mean)

#visar en graf med alla stats
#data.plot(title='Pokemon stats', kind='line')
#plt.ylabel('stats') # label = namnet på axeln
#plt.xlabel('Pokemon')
#plt.show()

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
# kräver extension Excel Viewer
# wb = Workbook()
# ws = wb.active
# with open('Pokemon.csv', 'r') as f:
#     for row in csv.reader(f):
#         ws.append(row)
# wb.save('Pokemon.xlsx')

# meny för att söka på en specifik pokemon och få fram all info om den
# while [1, 2]:
#     print("Sök på en Pokémon, 1. För att söka med nummer. 2. För att söka med namn.")
#     menu = int(input("Välj 1 eller 2: "))

#     if menu == 1:
#         print("Sök på Pokémon med nummer!")
#         userPoke = input()
#         data_indexed = pd.read_csv('Pokemon.csv', index_col="Name")
#         test = data_indexed.iloc[[userPoke]][['Type 1','Type 2','Total','HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', 'Generation', 'Legendary']] # söker på index
#         print(test)

#     elif menu == 2:
#         print("Sök på Pokémon med namn!") # Måste börja med stor bokstav
#         userPoke = input()
#         data_indexed = pd.read_csv('Pokemon.csv', index_col="Name")
#         test = data_indexed.loc[[userPoke]][['Type 1','Type 2','Total','HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', 'Generation', 'Legendary']] # söker på namn
#         print(test)
    
#     else:
#         print("Programmet avslutas")
#         break

print(data)