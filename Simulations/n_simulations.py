import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Constantes
g = 9.82  # Aceleración debido a la gravedad (m/s^2)
L = 1  # Longitud del péndulo (m)
m = 1 # Masa del péndulo (kg)
gamma = 10

def pendulum_derivatives(y, t, g, L, gamma, m, n):
    theta, omega = y
    dtheta_dt = omega
    domega_dt = - np.sign(omega) * (gamma) * np.abs(omega)**n - ((g / L) * np.sin(theta))
    return [dtheta_dt, domega_dt]

# Tiempo de simulación
t = np.linspace(0, 15, 1000)

plt.figure(figsize=(8, 6))

# Simulación y gráfico
y0 = [0.10, 0]  # Condiciones iniciales
colors = plt.cm.viridis(np.linspace(0, 1, 5))  

for i in range(1, 6):
    sol = odeint(pendulum_derivatives, y0, t, args=(g, L, gamma, m, i))  
    theta = sol[:, 0]  # Ángulo en el tiempo
    plt.plot(t, theta, color=colors[i-1], linestyle='--', linewidth=1.5, markersize=3, label=f'n = {i}')

# Configuración del gráfico
plt.title('Péndulo amortiguado: Ángulo vs Tiempo para diferentes valores de n')
plt.xlabel('Tiempo (s)')
plt.ylabel(r'$\theta$ (rad)')
plt.grid(True)
plt.legend()
plt.savefig(rf'Graficos\nvar.png', format=rf'Graficos\nvar.png'.split('.')[-1], dpi=300, bbox_inches='tight')
print(f"Gráfica 3D guardada en: {rf'Graficos\nvar.png'}")
plt.show()
