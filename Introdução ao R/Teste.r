#Análise da preferencia de alimentos de determinado animal
porcent <- c(30,60,15,5.6,3.8)#Porcentagem de disponivel de cada alimento
consumido <- c(257,607,110,78,62)#Consumo de cada item

tot.itens <- sum(consumido)#Total de itens consumido
esperado <- tot.itens*porcent/100
esperado#Valor esperado de consumo
desvio <- consumido - esperado
desvio#Desvio esperado

#Graficos comparando o esperado com o consumido
par(mfrow=c(1,2))
barplot(esperado)#Grafico do esperado
mtext("esperado", side=1, line=2, at=3,cex=1)
barplot(consumido)#Grafico do esperado
mtext("consumido", side=1, line=2, at=3,cex=1)
barplot(desvio)#grafico do desvio
mtext("desvio", side=1, line=2, at=3,cex=1)

#Graficos comparando o esperado com o desvio
par(mfrow=c(1,2))
barplot(esperado)#Grafico do esperado
mtext("esperado", side=1, line=2, at=3,cex=1)
barplot(desvio)#grafico do desvio
mtext("desvio", side=1, line=2, at=3,cex=1)

#Outro tipo de grafico
plot(esperado)
par(new=TRUE)
plot(desvio, axes=FALSE, ann=FALSE, pch=16)
mtext("desvio", side=4, line=2.5, at=-130,cex=1)
axis(4)

