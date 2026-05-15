import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Definimos las variables simbólicas (asumiendo a = 1 para el cálculo)
t = sp.Symbol('t')
a = 1 

# Ecuaciones paramétricas de la cardioide
x = a * (2 * sp.cos(t) - sp.cos(2 * t))
y = a * (2 * sp.sin(t) - sp.sin(2 * t))

# Derivada de x respecto a t
dx_dt = sp.diff(x, t)

# Planteamos la integral del área (multiplicada por 2 por simetría de 0 a pi)
# Fórmula: A = 2 * integral( y * dx/dt ) dt de 0 a pi
funcion_a_integrar = y * dx_dt
area_calculada = 2 * sp.integrate(funcion_a_integrar, (t, 0, sp.pi))

print(f"--- RESULTADO DEL CÁLCULO ---")
print(f"El área exacta calculada por Python (para a=1) es: {area_calculada}")
print(f"Nota: Como dejamos 'a' como 1, el resultado general es {area_calculada / sp.pi}*pi*a^2, es decir, 6*pi*a^2.\n")

t_num = np.linspace(0, 2 * np.pi, 1000)

# Ecuaciones en formato numérico (NumPy)
x_num = a * (2 * np.cos(t_num) - np.cos(2 * t_num))
y_num = a * (2 * np.sin(t_num) - np.sin(2 * t_num))

# Crear la figura
plt.figure(figsize=(8, 7))
plt.plot(x_num, y_num, color='darkred', linewidth=2, label='Cardioide')

# Sombrear la región entre la curva y el eje X (para visualizar la integración)
plt.fill_between(x_num, y_num, where=(t_num <= np.pi), color='crimson', alpha=0.3, label='Región de integración superior')
plt.fill_between(x_num, y_num, where=(t_num > np.pi), color='crimson', alpha=0.1, label='Región inferior (Simétrica)')

# Configuraciones de la gráfica
plt.axhline(0, color='black', linewidth=1, linestyle='--')
plt.axvline(0, color='black', linewidth=1, linestyle='--')
plt.title('Gráfica de la Cardioide y Área bajo la Curva', fontsize=14)
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.axis('equal') # Importante para que no se deforme la figura
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()

# Mostrar la gráfica
plt.savefig('grafica_cardioide.png', dpi=300)
#La grafica se guarda en el mismo directorio del script con el nombre 'grafica_cardioide.png'. Puedes abrirla con cualquier visor de imágenes.}
print("¡Gráfica guardada con éxito como 'grafica_cardioide.png'!")