import matplotlib.pyplot as plt

#Legendas
plt.title("Médias")
plt.xlabel("Matrícula")
plt.ylabel("Média")

pontos = open("Graficos PROEN/medias.csv").readlines()
#matricula
x = []
#media
y = []

for i in range(len(pontos)):
    if i != 0:
        linha = pontos[i].split(";")
        x.append(linha[0])
        y.append(float(linha[1]))

#Pontuação

#plt.scatter(x, y, color = "Black")
#plt.plot(x, y, label = "Pontos", linestyle = "-", color = "black")


plt.bar(x, y, label = "Nota média")

plt.legend()

plt.show()