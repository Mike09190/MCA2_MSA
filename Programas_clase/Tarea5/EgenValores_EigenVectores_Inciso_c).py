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

from sympy import Matrix, Rational
import numpy as np


# 1.- Cálculo de eigenvalores y eigenvectores directamente con numpy.linalg

# Definir una matriz cuadrada
# Definir la matriz de Hilbert del inciso a
# Para el inciso c)
A1 = np.array([[1, 2],
               [2, 4.0001]])

# Para SymPy (Exacto)
A2 = Matrix([[1, 2], 
             [2, Rational(40001, 10000)]])

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
print("\nMatriz  del inciso c) de eigenvectores: ")
P = A2.eigenvects()[0][2][0].row_join(A2.eigenvects()[1][2][0])
print("P  = ", P.tolist())