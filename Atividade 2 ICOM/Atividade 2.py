# -*- coding: utf-8 -*-
# Questão 1 - Resposta CSV.
# Questão 2 - Resposta Separado por vírgula.

# Questão 3 - Resposta abaixo.

import numpy as np

iris_data1 = np.genfromtxt('iris_data_1.csv', delimiter= ',')
iris_data2 = np.genfromtxt('iris_data_2.csv', delimiter= ',')

# Questão 4 - Resposta: Sim, está coreto! Código abaixo.

print (iris_data1.shape)
print (iris_data2.shape)

# Questão 5 - Resposta abaixo.

iris_data = np.vstack((iris_data1, iris_data2))

# Questão 6 - Resposta: Sim, está de acordo com o esperado! Código abaixo.

iris_data = np.vstack((iris_data1, iris_data2))

print (iris_data.shape)

# # Questão 7 - Resposta abaixo.

iris_data = iris_data[~np.isnan(iris_data).any(axis=1)]

# # Questão 8 - Resposta: Sim, está de acordo com o esperado. Código abaixo.

print (iris_data.shape)

# Questão 9 - Resposta abaixo.
# Incompleta

nodes, counts = np.unique(iris_data[:,5], return_counts=True)

print(f'São {len(nodes)} diferentes.\nOs valores são:{nodes}\nE se repetem {counts} respectivamente')


# Questão 10 - Resposta abaixo.

for x in range (3, -1, -1):
    iris_data[:,5][iris_data[:,5]==x] = (x + 1)
    
# Questão 11 - Resposta abaixo.

caracteristicas = iris_data [:,0:5]

print (caracteristicas.shape)

classes = iris_data [:,5:]

print (classes.shape)

# Questão 11 - Resposta abaixo.

np.savetxt('iris_data.csv', iris_data, delimiter=',')

