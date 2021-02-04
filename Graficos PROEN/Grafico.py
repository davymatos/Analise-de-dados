import matplotlib.pyplot as plt

#Legendas
plt.title("Pontuação média por questão")
plt.xlabel("Questões")
plt.ylabel("Pontuação")

pontos = open("Graficos PROEN/pontuacao.csv").readlines()
#Questões
x = []
#Pontos
y = []
#medias
xms = [-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
yms = [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]

xs = [-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
ys = [3.5,3.5,3.5,3.5,3.5,3.5,3.5,3.5,3.5,3.5,3.5,3.5,3.5,3.5,3.5,3.5,3.5,3.5,3.5,3.5,3.5,3.5]

for i in range(len(pontos)):
    if i != 0:
        linha = pontos[i].split(";")
        x.append(linha[0])
        y.append(float(linha[1]))

#Pontuação

#plt.scatter(x, y, color = "Black")
#plt.plot(x, y, label = "Pontos", linestyle = "-", color = "black")


plt.bar(x, y, label = "Pontos")
plt.plot(xms, yms, label = "Muito Satisfatório", linestyle = "-.", color = "Green")
plt.plot(xs, ys, label = "Satisfatório", linestyle = "--", color = "Orange")

plt.legend()

plt.show()