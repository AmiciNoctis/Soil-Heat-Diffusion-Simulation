# Analise computacional da difusão do calor no solo.

  Este repositório contém algoritmos em python para geração de gráficos para a análise da variação da temperatura em relação ao periodo de  e superfícies a difusão de calor no solo, utilizando a solução analítica obtida pelo princípio de Duhamel, uma abordagem alternativa para a obtenção de uma expressão fechada da solução exata de um problema de valores iniciais e de contorno (PVIC) para a equação de difusão unidimensional não homogênea com coeficientes constantes sujeitas a condições não homogêneas sobre um meio semi-infinito. Tal PVIC constitui um modelo inicial para a condução do calor no solo, o qual é resolvido por Ruth Brum (2013) por meio do método de separação de variáveis de Fourier. x'

## Visão Geral

  Seguindo Logan (2015), a abordagem alternativa sob estudo está baseada na solução fundamental (função de Green), a extensão antissimétrica da condição inicial, e nos princípios de Duhamel e de superposição. Este trabalho é um estudo preliminar para futuras aplicações em trocadores de calor solo-ar para conforto térmico em recintos fechados. A solução analítica obtida oferece uma representação detalhada da propagação do calor, permitindo uma compreensão mais profunda do fenômeno estudado. Além disso, a comparação com o método de Fourier, como utilizado por Brum (2013), destaca as vantagens e desvantagens de cada abordagem na resolução de problemas de transferência de calor.
	
  Embora ambos os métodos tenham sido eficazes na modelagem da difusão do calor no solo, a escolha entre eles pode depender das características específicas do problema e dos recursos computacionais disponíveis. O método de Duhamel pode ser mais adequado em situações onde as condições de contorno e as propriedades do meio variam com o tempo, enquanto o método de Fourier pode ser preferível em problemas com simetria e condições de contorno bem definidas.

## Conteúdo do Repositório

- `surf_u(z,t).py`: Este algoritmo calcula e plota a variação da temperatura no solo ao longo de um período de 365 dias em diferentes profundidades. Utilizando o método de integração numérica, a temperatura é calculada para cada ponto de tempo e profundidade especificados. Os resultados são então visualizados em um gráfico tridimensional e os dados são salvos em um arquivo .csv para análises adicionais.

- `erro_absoluto.py`: Gera a superfície de erro absoluto para visualizar a defasagem entre os valores da solução da Equação Diferencial Parcial (EDP) obtida pelo método de Duhamel e a solução obtida pelo método de

- `solucao_u(t)_Comparada.py`: Este algoritmo compara as soluções de temperatura no solo, obtidas por diferentes meios, e plota a evolução temporal da temperatura no solo em diferentes profundidades ao longo de vários dias. Utilizando métodos de integração numérica, a temperatura é calculada para cada profundidade especificada em intervalos de tempo fixos. Os resultados são plotados em um gráfico que mostra a variação da temperatura em relação à profundidade do solo para cada ponto de tempo especificado. Uma linha horizontal é adicionada para representar a média da temperatura.

- `solucao_u(z)_Comparada.py`: Este algoritmo compara as soluções de temperatura no solo obtidas através de diferentes abordagens. Além de calcular a temperatura utilizando um método de integração numérica, a solução de Ruth Brum (2013) também é implementada para efeito de comparação. Os resultados são plotados em um gráfico que mostra a variação da temperatura em relação à profundidade do solo, para dois pontos de tempo fixos. Uma linha horizontal é adicionada para representar a temperatura inicial de 18.7°C.

- `README.md`: Este arquivo que você está lendo, fornecendo uma visão geral do repositório.

- `Os parâmetros utilizados são`:

k = 0.057 # Constante de difusividade do solo
T = 365 # Tempo em dias
omega = 2 * np.pi / T # Periodo
theta0 = 6.28 # Amplitude
u0 = 18.7 # Média da temperatura do solo
