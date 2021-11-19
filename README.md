# Python_emotional_analysis
Este es un ejemplo de como hacer analisis de emociones usando python y varios modulos, es un primer aproximacion a este tema, el objetivo es demostrar ejemplos de como usar clasificadores bayesianos y regresiones lineales.

### Instalar:
Para instalar las dependencias del proyecto ejecute el siq. script:

```sh
pip install -r requirements.txt
```

### ¿Que es analisis de emociones?:
El análisis de emoción forma parte del Procesamiento del Lenguaje Natural (PLN) y de la tarea llamada Sentiment Analysis o análisis del sentimiento, y consiste en ir un paso más allá del análisis de la opinión (positiva, negativa o neutra) que estemos analizando.

### Dataset:
Se usan diversos datasets para generar distintos modelos usando clasificadores bayesianos.

**Playstore review - castellano**:
Gracias al trabajo de @ldubiau pude usar su lista de oraciones clasificadas,https://github.com/ldubiau/sentiment_classifier/tree/master/data2/output/pos en castellaño, estos datos provienen de reseñas de comentarios del playstore de android, ej: Guia Oleo, despegar.com, mercadolibre, etc.

**Playstore review - ingles**:
Gracias al trabajo de @Hrd2D podems obtener una lista de oraciones clasificadas por emociones, que sera usada luego para hacer predicciones, ej:https://github.com/Hrd2D/Sentiment-analysis-on-Google-Play-store-apps-reviews

**Tweets en ingles**:
Gracias al trabajo de @xxx podems obtener una lista de oraciones clasificadas por emociones, que sera usada luego para hacer predicciones, ej:https://github.com/Hrd2D/Sentiment-analysis-on-Google-Play-store-apps-reviews/blob/master/main.ipynb

### Comandos:
Podemos ejecutar los scripts para probar los diferentes modelos.

1) Probar modelo basado en **reviews de playstore - español**:
```sh
$ cd app_reviews_spanish
#Genero un json unificado.
$ python data_process.py
#Genero el modelo.
$ python model_generator.py
#Pruebo el modelo
$ python test_model.py
```

2) Probar modelo basado en **tweets en idioma ingles**:
```sh
$ cd tweets_english
#Genero el modelo.
$ python model_generator.py
#Pruebo el modelo
$ python test_model.py
```

3) Probar modelo basado en **reviews de playstore - ingles**:
```sh
$ cd app_reviews_english
#Genero el modelo.
$ python model_generator.py
#Pruebo el modelo
$ python test_model.py
```

4) Ejecutar pruebas de los datos generados.
```sh
python test_spanish_model.py
python test_english_model.py
```

### Referencias:
Uso como fuente de datos....

https://github.com/Hrd2D/Sentiment-analysis-on-Google-Play-store-apps-reviews/blob/master/main.ipynb
https://www.analyticsvidhya.com/blog/2021/07/performing-sentiment-analysis-with-naive-bayes-classifier/
https://levelup.gitconnected.com/movie-review-sentiment-analysis-with-naive-bayes-machine-learning-from-scratch-part-v-7bb869391bab
https://cnvrg.io/sentiment-analysis-python/
https://github.com/ldubiau/sentiment_classifier
https://42jaiio.sadio.org.ar/proceedings/simposios/Trabajos/ASAI/04.pdf <--
https://github.com/taljuk01/political_sentiment_analysis
https://github.com/manugarri/tweets_map
https://www.kaggle.com/kazanova/sentiment140
https://pybonacci.org/2015/11/24/como-hacer-analisis-de-sentimiento-en-espanol-2/
