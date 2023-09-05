import math
import matplotlib.pyplot as plt
import numpy as np

# Gerar valores de x no intervalo de 0 a 2*pi
x = np.linspace(0, 2 * math.pi, 1000)

# Calcular os valores do cosseno para cada valor de x
y = [math.cos(val) for val in x]

# Plotar o grafico
plt.plot(x, y)
plt.title('Grafico da Funcao Cosseno')
plt.xlabel('x')
plt.ylabel('cos(x)')
plt.grid(True)
plt.show()
