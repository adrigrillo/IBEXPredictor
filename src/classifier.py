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
from sklearn import svm


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


def automatic_cross_validation(X, Y, epochs, batch, splits):
    """
    Ejecucion del entrenamiento y test mediante cross validation
    :param X: Conjuntos de variables
    :param Y: Salida del conjunto de variables
    :return:
    """
    estimador = KerasClassifier(build_fn=create_model, nb_epoch=epochs, batch_size=batch, verbose=2)
    kfold = StratifiedKFold(n_splits=splits, shuffle=True, random_state=seed)
    results = cross_val_score(estimador, X, Y, cv=kfold)
    print("Resultados: %.2f%% (%.2f%%)" % (results.mean()*100, results.std()*100))
    saveModel(estimador.model)


def training_test_manual(trainX, testX, trainY, testY, epochs, batch):
    """
    Entrenamiento y evaluacion manual de el modelo creado
    :param trainX: variables de entrada de entrenamiento
    :param trainY: resultados de entrenamiento
    :param testX: variables de entrada de test
    :param testY: resultados de test
    :return:
    """
    model = create_model()
    model.fit(trainX, trainY, nb_epoch=epochs, batch_size=batch, verbose=2)
    resultados = model.evaluate(testX, testY, verbose=2)
    print("%s: %.2f%%" % (model.metrics_names[0], resultados[0]*100))
    print("%s: %.2f%%" % (model.metrics_names[1], resultados[1]*100))
    saveModel(model)


def support_vector_machine(trainX, testX, trainY, testY, kernel, C, gamma=0.1, degree=1):
    if kernel == 'linear':
        svc = svm.SVC(kernel=kernel, C=C).fit(trainX, trainY)
    if kernel == 'rbf':
        svc = svm.SVC(kernel=kernel, gamma=gamma, C=C).fit(trainX, trainY)
    if kernel == 'poly':
        svc = svm.SVC(kernel=kernel, degree=degree, C=C).fit(trainX, trainY)
    resultados = svc.score(testX, testY)
    print("Resultados: ", resultados*100, " %")


def selector(type_of_learning, fichero):
    if type_of_learning == 'auto_neural':
        X, Y = create_full_dataset(fichero, 30)
        automatic_cross_validation(X, Y, 200, 20, 5)
    if type_of_learning == 'man_neural':
        trainX, testX, trainY, testY = create_training_test_dataset(fichero, 30, 0.9)
        training_test_manual(trainX, testX, trainY, testY, 500, 20)
    if type_of_learning == 'svm':
        trainX, testX, trainY, testY = create_training_test_dataset(fichero, 30, 0.9)
        support_vector_machine(trainX, testX, trainY, testY, 'poly', 0.2, degree=3)

def main():
    numpy.random.seed(seed)
    fichero = "5DayNormal.csv"
    selector('svm', fichero)


if __name__ == '__main__':
    main()

