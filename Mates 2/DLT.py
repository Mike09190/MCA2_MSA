import numpy as np

def solve_dlt(points_3d, points_2d):
    """
    Resuelve la matriz de proyección P usando DLT.
    """
    A = []
    for i in range(len(points_3d)):
        X, Y, Z = points_3d[i]
        u, v = points_2d[i]
        
        # Las dos ecuaciones independientes por punto (m x PM = 0)
        A.append([X, Y, Z, 1, 0, 0, 0, 0, -u*X, -u*Y, -u*Z, -u])
        A.append([0, 0, 0, 0, X, Y, Z, 1, -v*X, -v*Y, -v*Z, -v])

    A = np.array(A)
    
    # Resolver mediante Descomposición en Valores Singulares (SVD)
    _, _, Vh = np.linalg.svd(A)
    # La solución es la última fila de Vh
    P = Vh[-1].reshape(3, 4)
    
    # Normalizar para que el último elemento sea 1 (opcional pero limpio)
    if P[-1, -1] != 0:
        P = P / P[-1, -1]
        
    return P

# --- DATOS DEL MODELO REAL BASADOS EN TU FOTO (Sencillo y Rápido) ---

# Coordenadas en el Mundo 3D (Caja estimada 15x8x3 cm)
# (X, Y, Z)
pts_3d = np.array([
    [0, 0, 0],   # M1: Origen (Esquina frontal inferior izquierda visible)
    [15, 0, 0],  # M2: Derecha base (Esquina frontal inferior derecha visible)
    [0, 8, 0],   # M3: Arriba izquierda frente (Esquina superior izquierda visible)
    [15, 8, 0],  # M4: Arriba derecha frente (Esquina superior derecha visible)
    [0, 0, 3],   # M5: Fondo izquierda base (Esquina lateral inferior izquierda visible)
    [15, 8, 3]   # M6: Esquina superior derecha fondo (Esquina trasera superior derecha visible, estimada)
])

# Coordenadas en Píxeles (Imagen 1920x1080, estimación de posición)
# (u, v)
pts_2d = np.array([
    [960, 800],  # m1
    [1400, 750], # m2
    [960, 450],  # m3
    [1400, 400], # m4
    [860, 850],  # m5
    [1300, 350]  # m6
])

# Ejecutar el cálculo DLT
matriz_P = solve_dlt(pts_3d, pts_2d)

# --- RESULTADOS PARA TU REPORTE ---
print("-" * 30)
print("MATRIZ DE PROYECCIÓN P CALCULADA (DLT):")
print("-" * 30)
# Imprimir con formato bonito
np.set_printoptions(suppress=True, precision=5)
print(matriz_P)
print("-" * 30)

# PRUEBA DE FUEGO: REPROYECCIÓN
print("\nPrueba de coherencia (Reproyectar Puntos):")
for i in range(len(pts_3d)):
    M_homo = np.append(pts_3d[i], 1) # Punto 3D en homogéneas
    m_repro = matriz_P @ M_homo      # m = P * M
    
    # Convertir de homogéneas a píxeles (dividir por w)
    w = m_repro[2]
    u_calc = m_repro[0] / w
    v_calc = m_repro[1] / w
    
    # Calcular error de reproyección
    error = np.sqrt((u_calc - pts_2d[i][0])**2 + (v_calc - pts_2d[i][1])**2)
    
    print(f"M{i+1}: Original ({pts_2d[i][0]}, {pts_2d[i][1]}) -> Calculado ({u_calc:.1f}, {v_calc:.1f}). Error: {error:.2f} px")