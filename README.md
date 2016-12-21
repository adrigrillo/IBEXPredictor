# PREDICTOR DEL IBEX-35
A ver, antes de leer estos articulos os aviso que vamos a necesitar librerias especiales de python para poder hacer 
cosas sin comernos la cabeza. Por eso teneis dos opciones, o importarlas vosotros manualmente o instalaros anaconda, 
que es python igual pero con las librerias ya añadidas, podeis descargarlo [aquí](https://www.continuum.io/downloads).

Para instalarlas manualmente podeis usar el siguiente comando:

    pip install -r requirements.txt

## Contenido
En este proyecto encontrarás:

- __dataGetter.py:__ Clase para obtener los datos de la bolsa.
- __classifier.py:__ Clase con los diferentes clasificadores con los que predecir la bolsa. Clasificadores disponibles:
    - Red de neuronas
    - Máquina de soporte vectorial 
    - Random Forest
    - kNN
- __ploter.py:__ Clase para representar los datos en una gráfica.
- __predictor.py:__ Clase con un modelo de regresión para predecir la bolsa.

## Funcionamiento
1. Obtener los datos mediante la clase _datagetter.py_
2. Configurar el clasificador deseado.
3. Ejecutar el entrenamiento y test de _clasiffier.py_