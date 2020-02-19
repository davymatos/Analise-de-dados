import matplotlib.pyplot as plt

x1 = [1, 2, 3, 4, 5]
y1 = [4, 3, 7, 5, 1]

x2 = [1, 2, 3, 4, 5]
y2 = [5, 2, 9, 1, 5]

x3 = [1, 2, 3, 4, 5]
y3 = [7, 5, 3, 3, 6]

titulo = "Gráfico"
eixox = "Eixo X"
eixoy = "Eixo Y"

#Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.scatter(x1, y1, marker = "*")
plt.plot(x1, y1, label = "Grupo 1", linestyle = "--")

plt.scatter(x2, y2, marker = "^")
plt.plot(x2, y2, label = "Grupo 2", linestyle = "--")

plt.scatter(x3, y3, color = "black")
plt.plot(x3, y3, label = "Grupo 3", linestyle = "--", color = "black")
plt.legend()

#plt.show()
plt.savefig("figura1.png")
