dados = read.csv("populacao-brasileira (1).csv", header=TRUE, sep=";")

#Crescimento da População
plot(dados$ano, dados$population, main = "População brasileira", xlab = "Ano", ylab = "População")

dadoss = as.factor(dados$population > 200000000)
summary(dadoss)

#Anos com mais de 200 Milhões de habitantes
plot(dadoss, main = "População maior que 200 Milhões(1980-2016)", xlab = "", ylab = "Quantidade Anos")



#-----Anos com mais 200 Milhões de habitantes(Outra Visualização)-----#
dadoss = read.csv("populacao-brasileira (1).csv", header=TRUE, sep=";")

dadoss = dados$population > 200000000
summary(dadoss)

plot(dadoss, main = "População maior que 200 Milhões(1980-2016)", xlab = "Quantidade Anos", ylab = "")

