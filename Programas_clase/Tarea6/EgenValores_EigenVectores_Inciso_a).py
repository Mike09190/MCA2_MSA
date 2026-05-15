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

from sympy import Matrix, S
import numpy as np


# 1.- Calculo de eigenvalores y eigenvectores directamente con numpy.linalg

# Definir una matriz cuadrada
# Definir la matriz de Hilbert del inciso a
A1 = np.array([[1, 1/2, 1/3],
               [1/2, 1/3, 1/4],
               [1/3, 1/4, 1/5]])
A2 = Matrix([[1, S(1)/2, S(1)/3], 
             [S(1)/2, S(1)/3, S(1)/4], 
             [S(1)/3, S(1)/4, S(1)/5]])

eigenvalores, eigenvectores = np.linalg.eig(A1)
print("\nEigenvalores y Eigenvectores con numpy \n")

print("Eigenvalores:\n", eigenvalores)
print("Eigenvectores unitarios:\n", eigenvectores)

# eigenvects() devuelve una lista de tuplas: 
# (eigenvalor, multiplicidad, [eigenvectores])
eigen_data = A2.eigenvects()

print("\nEigenvalores y Eigenvectores (en formato 'exacto')con sympy ")
for i, (val, mult, vecs) in enumerate(eigen_data):
    print(f"\nEl Eigenvalor {i+1} es: {val}")
    for j, vec in enumerate(vecs):
        # SymPy ya devuelve las fracciones simplificadas
        print(f"  Un eigenvector de {val} es: {vec.tolist()}")

# Presentar los vectores en forma de la matiz P.
print("\nMatriz  del inciso a) de eigenvectores: ")
P = A2.eigenvects()[0][2][0].row_join(A2.eigenvects()[1][2][0]).row_join(A2.eigenvects()[2][2][0])
print("P = ", P.tolist())
