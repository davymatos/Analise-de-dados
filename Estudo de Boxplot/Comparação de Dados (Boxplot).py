import matplotlib.pyplot as plt
import random

valores = [3,5,222,96,7,56,120,45,300]
n = []

for i in range(100):
    numero = random.randint(0,100)
    n.append(numero)

plt.boxplot(valores)
plt.show()