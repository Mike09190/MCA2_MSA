# -*- coding: utf-8 -*-
"""
Obtención eigenvalores y eigenvectores  y matriz  P (de aigenvectores) 
utilizando :
    cálculo numérico: numpy 
    caculo simbólico: sympy

Curso: MCA2 clases 23 y 25 marzo 2026. Notas 23 y 24 marzo

Readaptacíon del código visto en clase, para obtener los eigenvalores y eigenvectores del inciso a)

      
Referencias:
    - https://docs.sympy.org/latest/modules/matrices/matrices.html
    - Roe (1993). Elementary Geometry, Oxford University Press p. 152


Software:
    Python 3.14.3
    IDE    Spyder
    
@author: Roberto Méndez / Web
Created  Sun 23 Marzo 2026
Editada  9 Abril 2026
"""

from sympy import Matrix
import numpy as np


# 1.- Cálculo de eigenvalores y eigenvectores directamente con numpy.linalg

# Definir una matriz cuadrada
# Definir la matriz de Hilbert del inciso b
A1 = np.array([[1, 1, 1, 1],
               [1.01, 1.02, 1.03, 1.04],
               [1.01**2, 1.02**2, 1.03**2, 1.04**2],
               [1.01**3, 1.02**3, 1.03**3, 1.04**3]])

eigenvalores, eigenvectores = np.linalg.eig(A1)
print("\nEigenvalores y Eigenvectores con numpy \n")

print("Eigenvalores:\n", eigenvalores)
print("Eigenvectores unitarios:\n", eigenvectores)



# 2. Calcular los eigenvalores y eigenvectores utiizando sympy

A2 = Matrix(A1)
# eigenvects() devuelve una lista de tuplas: 
# (eigenvalor, multiplicidad, [eigenvectores])
eigen_data = A2.eigenvects()

print("\nEigenvalores y Eigenvectores (en formato 'exacto')con sympy ")
for i, (val, mult, vecs) in enumerate(eigen_data):
    print(f"\nEl Eigenvalor {i+1} es: {val}")
    for j, vec in enumerate(vecs):
        # SymPy ya devuelve las fracciones simplificadas
        print(f"  Un eigenvector de {val} es: {vec.tolist()}")


print("\nMatriz P de eigenvectores (inciso b): ")
# Extraemos los 4 vectores propios de SymPy
vecs_lista = [data[2][0] for data in eigen_data]
P = vecs_lista[0].row_join(vecs_lista[1]).row_join(vecs_lista[2]).row_join(vecs_lista[3])
print("P = ", P.tolist())