from fastapi import FastAPI
import pandas as pd
from starlette.responses import RedirectResponse

# cargo el DataSet
df_movies = pd.read_csv('movies_etl_api.csv')


app = FastAPI()

@app.get('/')
def raiz():
    # funcion que muestra el entorno grafico 
    return RedirectResponse(url="/docs/")

# funciones de consultas
@app.get('/peliculas_mes/{mes}')
def peliculas_mes(mes:str):
    filtered_movies = df_movies[df_movies['mes_es'] == mes.lower()]
    cantidad_peliculas = len(filtered_movies)
    return {'mes': mes, 'cantidad': cantidad_peliculas}  


@app.get('/peliculas_dia/{dia}')  # dis o dia
def peliculas_dia(dia:str):
    filtered_movies = df_movies[df_movies['dia_es'] == dia.lower()]
    cantidad_peliculas = len(filtered_movies)
    return {'dia': dia, 'cantidad': cantidad_peliculas}  


@app.get('/franquicia/{franquicia}')
def franquicia(franquicia:str):
    fran = df_movies[df_movies['name_franquicia'].str.contains(franquicia, case=False)]
    cantidad = len(fran)
    ganancia_total = fran['revenue'].sum()
    ganancia_promedio = ganancia_total / cantidad     
    
    return {'franquicia':franquicia, 'cantidad':cantidad, 
            'ganancia_total':ganancia_total, 
            'ganancia_promedio': ganancia_promedio}


@app.get('/peliculas_pais/{pais}')
def peliculas_pais(pais:str):
    pais_df = df_movies[df_movies['country_name'].str.contains(pais, case=False)]
    cantidad = pais_df.shape[0]
    return {'pais':pais, 'cantidad':cantidad}   



@app.get('/productoras/{productora}')
def productoras(productora:str):
    filtered_movies = df_movies[df_movies['name_production_compani'].str.contains(productora, case=False)]
    ganancia_total = filtered_movies['revenue'].sum()
    cantidad_peliculas = len(filtered_movies)
    return {'productora': productora, 'ganancia_total': ganancia_total, 'cantidad': cantidad_peliculas}
    



@app.get('/retorno/{pelicula}')
def retorno(pelicula):
    movie = df_movies[df_movies['title'] == pelicula]
    inversion = float(movie['budget'].iloc[0])
    ganancia  = float(movie['revenue'].iloc[0])
    retorno = float(movie['return'].iloc[0])
    anio = int(movie['release_year'].iloc[0])        
    
    return {'pelicula':pelicula, 'inversion':inversion, 'ganancia':ganancia,'retorno':retorno, 'anio':anio}


## Modelo ML 

# librerias 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from typing import List, Dict



@app.get('/recomendacion/{titulo}')
def recomendacion(titulo: str) -> Dict[str, List[str]]:
    # Obtener la fila de la película de entrada
    movie_row = df_movies.loc[df_movies['title'] == titulo]

    # Obtener el vector de características de la trama de la película de entrada
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(df_movies['overview'].dropna())
    movie_tfidf = vectorizer.transform(movie_row['overview'])

    # Calcular la similitud del coseno entre la película de entrada y todas las demás películas
    similarity_scores = cosine_similarity(movie_tfidf, tfidf_matrix)

    # Ordenar las películas por su similitud con la película de entrada y devolver las 5 más similares
    similar_indices = similarity_scores.argsort()[0][-6:-1]
    recommended_titles = list(df_movies.iloc[similar_indices]['title'].values)

    return {'recomendacion': recommended_titles}
