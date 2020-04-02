dados <- c(9,3,5,7,1,6,8,5,3)#Lista

max(dados)#Valor Maximo
min(dados)#valor Minimo
mean(dados)#Media
range(dados)#Valor Maximo e Minimo
diff(range(dados))#Taxa de Variação
sum(dados)#Soma
length(dados)#Quatidade de Valores da Lista
sum(dados)/length(dados)#Media com calculo
log(dados, base = 10)#logaritimo

sqrt(3)#Raiz Quadrada
sqrt(3:25)#Raizes Quadradas entre os numeros

search()#Pesquisa para verificação do caminho de busca
base::pi#Expecificação do pacote/Numero pi

normal.1 <- rnorm(10, mean = 10, sd = 2.5)#Simulação de amostra de 10 valores
range(normal.1)
diff(range(normal.1))