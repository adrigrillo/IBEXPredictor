#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy
import pandas as pd
import datetime
import _pickle as cPickle
from keras.models import Sequential
from keras.layers import *
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn import neighbors


""" Corregimos semilla """
seed = 7
root = '../data/'


def create_full_dataset(archivo, variables):
    """
    Este metodo devuelve todos los datos en un solo conjunto con las variables de entrada por un lado y la salida
    por otro.
    :param archivo: fichero donde se encuentran los datos
    :param variables: numero de variables de entrada
    :return: values donde estan las variables de entrada, result donde se encuentran el resultado de cada entrada
    """
    data = pd.read_csv(filepath_or_buffer=root+archivo, index_col='Date', parse_dates=True)
    dataset = data.values
    values = dataset[:,0:variables].astype(float)
    result = dataset[:,variables]
    return values, result


def create_training_test_dataset(archivo, variables, split):
    """
    Metodo que crea los diferentes de entrenamiento y test dado un porcentaje de division
    :param archivo: fichero donde se encuentran los datos
    :param variables: numero de variables de entrada
    :param split: porcentaje del total de instancias que contendra el conjunto de test
    :return: conjuntos de entrenamiento y test, por un lado las variables y por otro el resultado
    """
    data = pd.read_csv(filepath_or_buffer=root+archivo, index_col='Date', parse_dates=True)
    dataset = data.values
    values = dataset[:,0:variables].astype(float)
    result = dataset[:,variables]
    train_size = int(len(values) * split)
    trainX, testX = values[0:train_size], values[train_size:len(data)]
    trainY, testY = result[0:train_size], result[train_size:len(data)]
    return trainX, testX, trainY, testY


def create_model():
    """
    Creamos modelo de la red de neuronas con las capas de entrada y salida en Keras
    :return: Modelo de la red de neuronas
    """
    model = Sequential()
    model.add(Dense(6, input_dim=6, init='normal', activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(3, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(1, init='normal', activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='Adam', metrics=['accuracy'])
    return model


def saveModel(model, type):
    """
    Metodo que guarda el modelo por si quiere ser usado posteriormente
    :param model: modelo utilizado
    :return:
    """
    fecha = datetime.datetime.now().strftime("%d_%H:%M")
    fichero = root + "Models/model" + fecha
    if type == 1:
        model.save(fichero + ".h5")
    if type == 2:
        with open(fichero, 'wb') as f:
            cPickle.dump(model, f, -1)


def automatic_cross_validation(X, Y, epochs=200, batch=20, splits=5):
    """
    Ejecucion del entrenamiento y test mediante cross validation
    :param X: Conjuntos de variables
    :param Y: Salida del conjunto de variables
    :return:
    """
    estimador = KerasClassifier(build_fn=create_model, nb_epoch=epochs, batch_size=batch, verbose=0)
    kfold = StratifiedKFold(n_splits=splits, shuffle=True, random_state=seed)
    results = cross_val_score(estimador, X, Y, cv=kfold)
    print("Resultados: %.2f%% (%.2f%%)" % (results.mean()*100, results.std()*100))
    #saveModel(estimador.model, 1)


def training_test_manual(trainX, testX, trainY, testY, epochs=500, batch=20):
    """
    Entrenamiento y evaluacion manual de el modelo creado
    :param trainX: variables de entrada de entrenamiento
    :param trainY: resultados de entrenamiento
    :param testX: variables de entrada de test
    :param testY: resultados de test
    :return:
    """
    model = create_model()
    model.fit(trainX, trainY, nb_epoch=epochs, batch_size=batch, verbose=0)
    resultados = model.evaluate(testX, testY, verbose=0)
    print("%s: %.2f%%" % (model.metrics_names[0], resultados[0]*100))
    print("%s: %.2f%%" % (model.metrics_names[1], resultados[1]*100))
    saveModel(model, 1)


def support_vector_machine(trainX, testX, trainY, testY, kernel, C, gamma=0.1, degree=1):
    """
    Metodo para solucionar el problema mediante una maquina de soporte vectorial, ya sea linear, de base radial o
    polinomica
    :param trainX: variables de entrada de entrenamiento
    :param trainY: resultados de entrenamiento
    :param testX: variables de entrada de test
    :param testY: resultados de test
    :param kernel: kernel a elegir
    :param C: [0-1] rigidez para admitir clasificaciones incorrectas 0 es rigido
    :param gamma: Influencia de un ejemplo en el resto
    :param degree: Grado de polinomio, se refleja en el numero de dimensiones
    :return:
    """
    if kernel == 'linear':
        svc = svm.SVC(kernel=kernel, C=C, verbose=0, cache_size=600).fit(trainX, trainY)
    if kernel == 'rbf':
        svc = svm.SVC(kernel=kernel, gamma=gamma, C=C, verbose=1, cache_size=600).fit(trainX, trainY)
    if kernel == 'poly':
        svc = svm.SVC(kernel=kernel, degree=degree, C=C, verbose=1, cache_size=600).fit(trainX, trainY)
    resultados = svc.score(testX, testY)
    print("Resultados: ", resultados*100, " %")
    saveModel(svc, 2)


def random_forest(trainX, testX, trainY, testY, estimadores=1000):
    """
    Metodo para solucionar el problema mediante un clasificador random forest
    :param trainX: variables de entrada de entrenamiento
    :param trainY: resultados de entrenamiento
    :param testX: variables de entrada de test
    :param testY: resultados de test
    :param estimadores: Numero de veces que se ejecutara la tarea
    :return:
    """
    rfc = RandomForestClassifier(n_estimators=estimadores, n_jobs=-1, verbose=0)
    rfc.fit(trainX, trainY)
    resultados = rfc.score(testX, testY)
    print("Resultados: ", resultados*100, " %")
    saveModel(rfc, 2)


def nearest_neighbors(trainX, testX, trainY, testY, vecinos=3, algoritmo='auto'):
    """
    Metodo para solucionar el problema mediante un clasificador knn
    :param trainX: variables de entrada de entrenamiento
    :param trainY: resultados de entrenamiento
    :param testX: variables de entrada de test
    :param testY: resultados de test
    :param vecinos: numero de vecinos a tener en cuenta
    :param algoritmo: algoritmo a utilizar [‘auto’, ‘ball_tree’, ‘kd_tree’, ‘brute’]
    :return:
    """
    knn = neighbors.KNeighborsClassifier(n_neighbors=vecinos, algorithm=algoritmo, n_jobs=-1)
    knn.fit(trainX, trainY)
    resultados = knn.score(testX, testY)
    print("Resultados: ", resultados*100, " %")
    saveModel(knn, 2)


def selector(type_of_learning, fichero, entradas):
    """
    Metodo para seleccionar un algoritmo para la clasificacion dado un fichero
    :param type_of_learning: algoritmos a utilizar
    :param fichero: nombre del fichero en la carpeta data
    :return:
    """
    if type_of_learning == 'auto_neural':
        X, Y = create_full_dataset(fichero, entradas)
        automatic_cross_validation(X, Y)
    else:
        trainX, testX, trainY, testY = create_training_test_dataset(fichero, entradas, 0.9)
        if type_of_learning == 'man_neural':
            training_test_manual(trainX, testX, trainY, testY, epochs=500)
        if type_of_learning == 'svm':
            support_vector_machine(trainX, testX, trainY, testY, 'linear', 0.2, gamma=0.3, degree=3)
        if type_of_learning == 'rfc':
            random_forest(trainX, testX, trainY, testY, estimadores=10000)
        if type_of_learning == 'knn':
            nearest_neighbors(trainX, testX, trainY, testY, vecinos=1)


def main():
    numpy.random.seed(seed)
    fichero = ["ProcessedNormal.csv", "ProcessedChange.csv", "ProcessedRChange.csv", "ProcessedNormalized.csv"]
    fichero2 = ["5DayNormal.csv", "5DayChange.csv", "5DayRChange.csv", "5DayNormalized.csv"]
    type_learning = ['auto_neural', 'man_neural', 'svm', 'rfc', 'knn']
    """ for i in range(len(fichero)):
        for j in range(len(type_learning)):
            selector(type_of_learning=type_learning[j], fichero=fichero[i], entradas=6)
            selector(type_of_learning=type_learning[j], fichero=fichero2[i], entradas=30)
    """
    selector(type_of_learning=type_learning[1], fichero=fichero2[2], entradas=60)



if __name__ == '__main__':
    main()
