import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import quad, dblquad

# Definindo os parâmetros
k = 0.057 # Constante de difusividade do solo
T = 365 # Tempo em dias
omega = 2 * np.pi / T # Periodo
theta0 = 6.28 # Amplitude
u0 = 18.7 # Média da temperatura do solo

# Definindo a função a ser integrada
def v1_zt(y, tau, t, z):
    return np.cos(omega * tau + theta0) * (
        (1 / np.sqrt(4 * np.pi * k * (t - tau))) * np.exp(-((z - y)**2) / (4 * k * (t - tau))) -
        (1 / np.sqrt(4 * np.pi * k * (t - tau))) * np.exp(-((z + y)**2) / (4 * k * (t - tau)))
    )

# Definindo a função da segunda integral
def v2_zt(y, t):
    return (1 / np.sqrt(4 * np.pi * k * t)) * (np.exp(-((z - y)**2) / (4 * k * t)) - np.exp(-((z + y)**2) / (4 * k * t)))

# Definindo a função de temperatura com a contribuição adicional da segunda integral
def temperatura_u(t, z):
    # Calculando a primeira integral
    integral1, _ = dblquad(v1_zt, 0.1, t, lambda tau: 0.1, lambda tau: np.inf, args=(t, z)) # type: ignore

    # Calculando a segunda integral
    integral2, _ = quad(v2_zt, 0.1, np.inf, args=(t,))

    # Calculando o erro absoluto
    erro_absoluto = abs(-omega * theta0 * integral1 - (theta0 * np.exp(-np.sqrt(omega/(2*k))*z) * np.sin(np.sqrt(omega/(2*k))*z))*integral2 +
                        theta0 * np.sin(omega * t + theta0) - (theta0 * np.exp(-np.sqrt(omega/(2*k))*z) * np.sin(omega*t - np.sqrt(omega/(2*k))*z)))

    return erro_absoluto  # Calcula o módulo do erro absoluto

# Definindo valores de tempo e profundidade
t_values = np.linspace(0.1, 365, 100)  # Valores de tempo de 0 a 365 dias
z_values = np.linspace(0.1, 15, 100)    # Valores de profundidade de 0 a 15 metros

# Calculando os valores do módulo do erro absoluto para cada combinação de tempo e profundidade
erro_absoluto_values = np.zeros((len(z_values), len(t_values)))
for i, z in enumerate(z_values):
    for j, t in enumerate(t_values):
        erro_absoluto_values[i, j] = temperatura_u(t, z)

#Salvando os dados em um arquivo .csv
data_array = np.column_stack((t_values, erro_absoluto_values, z_values))
np.savetxt('dados_de_erro.csv', data_array, delimiter=',', header='Tempo, Erro, Profundidade', comments='')


# Plotando a superfície tridimensional do módulo do erro absoluto
T, Z = np.meshgrid(t_values, z_values)
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(T, erro_absoluto_values, Z, cmap='viridis') # type: ignore
ax.set_xlabel('Tempo (dias)')
ax.set_ylabel('Erro Absoluto')
ax.set_zlabel('Profundidade (metros)') # type: ignore
ax.set_title('Superfície de Erro Absoluto da Temperatura no Solo')
plt.show()