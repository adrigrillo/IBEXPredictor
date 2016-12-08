#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy
import pandas as pd
import datetime
from keras.models import Sequential
from keras.layers import *
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold


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
    model.add(Dense(30, input_dim=30, init='normal', activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(15, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(1, init='normal', activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model


def saveModel(model):
    """
    Metodo que guarda el modelo por si quiere ser usado posteriormente
    :param model: modelo utilizado
    :return:
    """
    fecha = datetime.datetime.now().strftime("%d_%H:%M")
    model.save(root + "Models/model" + fecha + ".h5")


def automatic_cross_validation(X, Y):
    """
    Ejecucion del entrenamiento y test mediante cross validation
    :param X: Conjuntos de variables
    :param Y: Salida del conjunto de variables
    :return:
    """
    estimador = KerasClassifier(build_fn=create_model, nb_epoch=200, batch_size=5, verbose=2)
    kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state=seed)
    results = cross_val_score(estimador, X, Y, cv=kfold)
    print("Resultados: %.2f%% (%.2f%%)" % (results.mean()*100, results.std()*100))
    saveModel(estimador.model)


def training_test_manual(trainX, testX, trainY, testY):
    """
    Entrenamiento y evaluacion manual de el modelo creado
    :param trainX: variables de entrada de entrenamiento
    :param trainY: resultados de entrenamiento
    :param testX: variables de entrada de test
    :param testY: resultados de test
    :return:
    """
    model = create_model()
    model.fit(trainX, trainY, nb_epoch=500, batch_size=20, verbose=2)
    resultados = model.evaluate(testX, testY, verbose=2)
    print("%s: %.2f%%" % (model.metrics_names[0], resultados[0]*100))
    print("%s: %.2f%%" % (model.metrics_names[1], resultados[1]*100))
    saveModel(model)

# TODO: Hacer otros metodos de clasificacion


def main():
    numpy.random.seed(seed)
    fichero = "5DayRChange.csv"
    """trainX, testX, trainY, testY = create_training_test_dataset(fichero, 30, 0.9)
    training_test_manual(trainX, testX, trainY, testY)"""
    X, Y = create_full_dataset(fichero, 30)
    automatic_cross_validation(X, Y)


if __name__ == '__main__':
    main()

