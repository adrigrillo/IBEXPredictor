#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold


def create_model():
    """
    Creamos modelo de la red de neuronas con las capas de entrada y salida en Keras
    :return: Modelo de la red de neuronas
    """
    model = Sequential()
    model.add(Dense(6, input_dim=6, init='normal', activation='relu'))
    model.add(Dense(1, init='normal', activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

def main():
    """ Corregimos semilla """
    seed = 7
    np.random.seed(seed)

    """ Cargamos los datos """
    data = pd.read_csv("../data/ProcessedRChange.csv", index_col='Date', parse_dates=True)
    dataset = data.values
    X = dataset[:,0:6].astype(float)
    Y = dataset[:,6]

    # evaluate model with standardized dataset
    estimator = KerasClassifier(build_fn=create_model, nb_epoch=100, batch_size=5, verbose=2)
    kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state=seed)
    results = cross_val_score(estimator, X, Y, cv=kfold)
    print("Results: %.2f%% (%.2f%%)" % (results.mean()*100, results.std()*100))

if __name__ == '__main__':
    main()


