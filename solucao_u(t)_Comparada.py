import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad, dblquad

# Definindo os parâmetros
k = 0.057
T = 365  # Período em dias
omega = 2 * np.pi / T
theta0 = 6.28
u0 = 18.7

# Definindo a função a ser integrada
def v1_zt(y, tau, t, z):
    return np.cos(omega * tau) * (
        (1 / np.sqrt(4 * np.pi * k * (t - tau))) * np.exp(-((z - y)**2) / (4 * k * (t - tau))) -
        (1 / np.sqrt(4 * np.pi * k * (t - tau))) * np.exp(-((z + y)**2) / (4 * k * (t - tau)))
    )

# Definindo a função da segunda integral
def v2_zt(y, t):
    return (1 / np.sqrt(4 * np.pi * k * t)) * (np.exp(-((z - y)**2) / (4 * k * t)) -
                                                np.exp(-((z + y)**2) / (4 * k * t)))
 
# Definindo a função de temperatura com a contribuição adicional da segunda integral
def temperatura_u(t, z):
    # Calculando a primeira integral
    integral1, _ = dblquad(v1_zt, 0, t, lambda tau: 0, lambda tau: np.inf, args=(t, z))  # type: ignore

    # Calculando a segunda integral
    integral2, _ = quad(v2_zt, 0, np.inf, args=(t,))

    # Calculando a temperatura total
    temperatura_total = (-omega * theta0 * integral1 - (theta0 * np.exp(-np.sqrt(omega/(2*k))*z) * np.sin(np.sqrt(omega/(2*k))*z))*integral2 +
                          u0 + theta0 * np.sin(omega * t))

    return temperatura_total

# Definindo a solução analítica a ser comparada  
def solucao_Temperatura(z, t):
    return u0 + (theta0 * np.exp(-np.sqrt(omega/(2*k))*z)) * np.sin(omega*t - np.sqrt(omega/(2*k))*z)

# Definindo valores de tempo
t_values = np.linspace(1, 365, 100)  # Valores de tempo de 0 a 365 dias

# Definindo valores de profundidade
z_values = [0.5, 0.8, 1, 1.5, 2, 2.4, 3]  # Valores de profundidade de 0 a 3 metros

# Plotando os gráficos para cada valor de profundidade e a solução analítica
plt.figure(figsize=(10, 6))
for z in z_values:
    temperatura_z_values = [temperatura_u(t, z) for t in t_values]
    plt.plot(t_values, temperatura_z_values, label=f'z={z}')
    # Plotando linhas tracejadas para as profundidades de referência (zr)
    plt.plot(t_values, [solucao_Temperatura(z, t) for t in t_values], linestyle='--', color=plt.gca().lines[-1].get_color())

plt.xlabel('Tempo (dias)')
plt.ylabel('Temperatura (°C)')
plt.title('Temperatura no solo em diferentes profundidades durante 365 dias')   
plt.grid(True)
plt.legend()
plt.show()
