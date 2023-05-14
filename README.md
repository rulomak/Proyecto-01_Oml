# Machine Learning Operations (MLOps)
Este proyecto consiste en una API construida con FastAPI, que permite consultar información sobre películas. Los datos se obtuvieron a partir de un dataset en formato CSV, al cual se le realizó un ETL básico para extraer algunos datos anidados. A continuación, se realizó un EDA para explorar los datos y se construyó la API con 7 endpoints disponibles:

## Uso

### Interfaz gráfica

La API incluye una interfaz gráfica. Para acceder a ella, abre un navegador y dirígete a: https://recomendaciones-api.onrender.com  donde está alojada la API.  
Una vez allí, podrás explorar los diferentes endpoints disponibles, así como hacer pruebas y consultas.

### Endpoints

La API cuenta con los siguientes endpoints:

- `películas_mes`: recibe el nombre de un mes y devuelve una lista de películas estrenadas en ese mes.
- `películas_dia`: recibe el nombre de un día y devuelve una lista de películas estrenadas en ese día.
- `franquicia`: recibe el nombre de una franquicia y devuelve información sobre la cantidad de películas, ganancias totales y ganancia promedio de la franquicia.
- `películas_pais`: recibe el nombre de un país y devuelve información sobre la cantidad de películas producidas en ese país.
- `productoras`: recibe el nombre de una productora y devuelve información sobre las ganancias totales y cantidad de películas producidas por la misma.
- `retorno`: recibe el nombre de una película y devuelve información sobre inversión, ganancias, retorno y año de estreno.
- `recomendación`: recibe el nombre de una película y devuelve una lista de 5 películas similares según un modelo de Machine Learning.

Cada endpoint tiene un conjunto específico de parámetros y devuelve una respuesta en formato JSON con la información correspondiente.

## Contribución

Si deseas contribuir al proyecto, por favor sigue estos pasos:

1. Haz un fork del repositorio. :: https://github.com/rulomak/Proyecto-01_Oml
2. Crea una rama para tus cambios: `git checkout -b mi-rama`
3. Realiza los cambios necesarios y haz commit: `git commit -am "Descripción de los cambios"`
4. Realiza un push a la rama: `git push origin mi-rama`
5. Crea un pull request en GitHub.

## Autor

- Raul Abelleira