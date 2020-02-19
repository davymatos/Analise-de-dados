#Crescimento da população Brasileira 80 - 2016
#Dados do DATASUS
import matplotlib.pyplot as plt

dados = open("populacao-brasileira (1).csv").readlines()

plt.title("Crescimento Populacional(1980 - 2016)")
plt.xlabel("ANOS")
plt.ylabel("POPULAÇÃO - Escala 100 000 000")
#Ano
x = []
#População
y = []

for i in range(len(dados)):
    if i != 0:
        linha = dados[i].split(";")
        x.append(int(linha[0]))
        y.append(int(linha[1]))

plt.plot(x, y, color = "black", linestyle = "--")
plt.bar(x, y, color = "#999999")
plt.show()
#plt.savefig("População-brasileira.pdf")