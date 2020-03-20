import pandas as pd

#uri = "https://raw.githubusercontent.com/SkwD1/Analise-de-dados/master/Crescimento%20da%20popula%C3%A7%C3%A3o/populacao-brasileira%20(1).csv"
uri = "https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula3.1/movies.csv"
filmes = pd.read_csv(uri)
filmes.columns = ["filme_id", "titulo", "generos"]
filmes.head()

uri = "https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula4.1/ratings.csv"
notas = pd.read_csv(uri)
notas.columns = ["usuario_id", "filme_id", "nota", "tempo"]
notas["nota"].head()
notas["nota"].unique()
notas["nota"].mean()
notas["nota"].min()
notas["nota"].max()
notas.describe()
#notas.nota.plot(kind="hist")