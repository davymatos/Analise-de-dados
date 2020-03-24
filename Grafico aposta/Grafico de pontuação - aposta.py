import matplotlib.pyplot as plt

#Legendas
plt.title("Pontuação Acumulada da Aposta")
plt.xlabel("Data")
plt.ylabel("Pontos")

pontosa = open("pontuacao_aposta_alisson.csv").readlines()
#Data
xa = []
#Pontos
ya = []
acuma = []

for i in range(len(pontosa)):
    if i != 0:
        linha = pontosa[i].split(";")
        xa.append(linha[0])
        ya.append(float(linha[1]))

somaa = 0
for j in ya:
    somaa += j
    acuma.append(somaa)

pontosj = open("pontuacao_aposta_junior.csv").readlines()
#Data
xj = []
#Pontos
yj = []
acumj = []

for i in range(len(pontosj)):
    if i != 0:
        linha = pontosj[i].split(";")
        xj.append(linha[0])
        yj.append(float(linha[1]))

somaj = 0
for j in yj:
    somaj += j
    acumj.append(somaj)

pontosc = open("pontuacao_aposta_cleiton.csv").readlines()
#Data
xc = []
#Pontos
yc = []
acumc = []

for i in range(len(pontosc)):
    if i != 0:
        linha = pontosc[i].split(";")
        xc.append(linha[0])
        yc.append(float(linha[1]))

somac = 0
for j in yc:
    somac += j
    acumc.append(somac)

pontos = open("pontuacao_aposta_davy.csv").readlines()
#Data
x = []
#Pontos
y = []
acum = []

for i in range(len(pontos)):
    if i != 0:
        linha = pontos[i].split(";")
        x.append(linha[0])
        y.append(float(linha[1]))

soma = 0
for j in y:
    soma += j
    acum.append(soma)


'''
#Pontuação diaria
plt.scatter(x, y, marker = "^")
plt.plot(x, y, label = "Davy", linestyle = "--")

plt.scatter(xa, ya, marker = "*")
plt.plot(xa, ya, label = "Alisson", linestyle = "--")

plt.scatter(xj, yj, marker = "^")
plt.plot(xj, yj, label = "Junior", linestyle = "--")

plt.scatter(xc, yc, color = "black")
plt.plot(xc, yc, label = "Cleiton", linestyle = "--", color = "black")
plt.legend()
'''

#Pontuação Acumulada
plt.scatter(x, acum, marker = "^")
plt.plot(x, acum, label = "Davy", linestyle = "--")

plt.scatter(xa, acuma, marker = "*")
plt.plot(xa, acuma, label = "Alisson", linestyle = "--")

plt.scatter(xj, acumj, marker = "^")
plt.plot(xj, acumj, label = "Junior", linestyle = "--")

plt.scatter(xc, acumc, color = "black")
plt.plot(xc, acumc, label = "Cleiton", linestyle = "--", color = "black")
plt.legend()

plt.show()
