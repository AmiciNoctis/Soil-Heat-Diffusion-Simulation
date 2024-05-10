import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad, dblquad

# Definindo os parâmetros
k = 0.057 # Constante de difusividade do solo
T = 365 # Tempo em dias
omega = 2 * np.pi / T # Periodo
theta0 = 6.28 # Amplitude
u0 = 18.7 # Média da temperatura do solo

# Definindo a função a ser integrada
def v1_zt(y, tau, t, z):
    return np.cos(omega * tau) * (
        (1 / np.sqrt(4 * np.pi * k * (t - tau))) * np.exp(-((z - y)**2) / (4 * k * (t - tau))) -
        (1 / np.sqrt(4 * np.pi * k * (t - tau))) * np.exp(-((z + y)**2) / (4 * k * (t - tau)))
    )

# Definindo a função de temperatura com a contribuição adicional da segunda integral
def temperatura_u(t, z):
    # Calculando a primeira integral
    integral1, _ = dblquad(v1_zt, 0, t, lambda tau: 0, lambda tau: np.inf, args=(t, z)) # type: ignore

    # Calculando a segunda integral
    integral2, _ = quad(lambda y, t: (1 / np.sqrt(4 * np.pi * k * t)) * (np.exp(-((z - y)**2) / (4 * k * t)) -
                                                                     np.exp(-((z + y)**2) / (4 * k * t))), 0, np.inf, args=(t,))

    # Calculando a temperatura total
    temperatura_total = (-omega * theta0 * integral1 - (theta0 * np.exp(-np.sqrt(omega/(2*k))*z) * np.sin(np.sqrt(omega/(2*k))*z))*integral2 +
                          u0 + theta0 * np.sin(omega * t))

    return temperatura_total

# Definindo valores de tempo fixo
t_fixed = [30, 90, 120, 150]  # Tempo fixo em dias

# Definindo valores de profundidade
z_values = np.linspace(0, 15, 100)  # Valores de profundidade de 0 a 15 metros

# Plotando as curvas de temperatura para cada valor de t_fixed
plt.figure(figsize=(10, 6))
for t in t_fixed:
    temperaturas = [temperatura_u(t, z) for z in z_values]
    plt.plot(z_values, temperaturas, label=f'Dia {t}')

# Adicionando a linha horizontal em 18.7 graus
plt.axhline(y=u0, color='r', linestyle='--', label='18.7°C')

plt.xlabel('Profundidade (m)')
plt.ylabel('Temperatura (°C)')
plt.title('Temperatura no solo em diferentes dias')
plt.legend()
plt.grid(True)
plt.show()