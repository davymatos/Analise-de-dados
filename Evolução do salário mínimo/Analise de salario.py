import matplotlib.pyplot as plt

dados = open("valores.csv").readlines()
plt.title("Troca de Moeda no Brasil")
plt.xlabel("Tempo")
plt.ylabel("Moedas")

#Moeda
x = []
#Salario
y = []

for i in range(len(dados)):
    if i != 0:
        linha = dados[i].split(";")
        x.append(linha[0])
        #y.append(linha[1])

plt.plot(x, color = "black", linestyle = "--")
plt.show()