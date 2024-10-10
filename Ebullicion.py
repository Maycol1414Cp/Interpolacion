import numpy as np
import matplotlib.pyplot as plt

# Datos de la tabla
h = np.array([-1000, 0, 3000, 8000, 15000, 22000, 28000])  # Alturas en pies
T = np.array([213.9, 212, 206.2, 196.2, 184.4, 172.6, 163.1])  # Temperaturas en °F

# Punto donde queremos estimar la temperatura 
h_5000m = 16404.2
LaPaz=11942.2
ElAlto=13615.4

# Función de interpolación de Lagrange
def lagrange_interpolation(x, x_points, y_points):
    total_sum = 0
    n = len(x_points)
    for i in range(n):
        term = y_points[i]
        for j in range(n):
            if i != j:
                term *= (x - x_points[j]) / (x_points[i] - x_points[j])
        total_sum += term
    return total_sum

# Crear la gráfica
plt.figure(figsize=(8,6))
plt.plot(h, T, 'bo-', label='Datos originales')

# Etiquetas y título
plt.title('Boiling Temperature vs Altitude', fontsize=14)
plt.xlabel('Altitude (ft)', fontsize=12)
plt.ylabel('Boiling Temperature (°F)', fontsize=12)
plt.grid(True)

# Estimar la temperatura y añadirla al gráfico
T_5000m = lagrange_interpolation(h_5000m, h, T)
plt.plot(h_5000m, T_5000m, 'ro', label=f'Estimación a 5000m: {T_5000m:.2f} °F')
TElAlto = lagrange_interpolation(ElAlto, h, T)
plt.plot(ElAlto, TElAlto, 'ro', label=f'Estimación en El Alto: {TElAlto:.2f} °F')
TLaPaz = lagrange_interpolation(LaPaz, h, T)
plt.plot(LaPaz, TLaPaz, 'ro', label=f'Estimación en La Paz: {TLaPaz:.2f} °F')
# Mostrar leyenda
plt.legend()

# Mostrar la gráfica
plt.savefig('EbullicionG.png', dpi=300)
