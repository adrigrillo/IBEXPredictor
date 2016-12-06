#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math as mt
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error

# fix random seed for reproducibility
np.random.seed(7)

def loadData():
    """
    Metodo que lee los datos para posteriormente poder usarlos, cambia la fecha de
    texto a datetime.
    :return: Datos con respecto al cambio del dia anterior y datos en valores
    """
    transFecha = lambda fecha: pd.datetime.strptime(fecha, '%Y-%m-%d')
    dataReal = pd.read_csv('../data/Ibex35Normal', engine='python', parse_dates=[0], index_col=0,
                            date_parser=transFecha, usecols=[0,6], skipfooter=3)
    adjClose = pd.read_csv('../data/Ibex35RChange', usecols=[6], engine='python')
    dataChange = adjClose.values
    return dataChange, dataReal


def traning_test(datos):
    """
    Metodo que establecera los conjuntos de test y entrenamiento
    :param datos: Datos de la bolsa
    :return: conjuntos de entrenamiento y test
    """
    train_size = int(len(datos) * 0.7)
    train, test = datos[0:train_size,:], datos[train_size:len(datos),:]
    print("Conjunto de entrenamiento, longitud: ", len(train))
    print("Conjunto de test, longitud: ",  len(test))
    return train, test


# convert an array of values into a dataset matrix
def crearDataset(dataset, vista_atras):
    dataX, dataY = [], []
    for i in range(len(dataset)-vista_atras-1):
        a = dataset[i:(i+vista_atras), 0]
        dataX.append(a)
        dataY.append(dataset[i + vista_atras, 0])
    return np.array(dataX), np.array(dataY)


def lstm(trainX, trainY, testX, testY, change, vista_atras):
    # create and fit the LSTM network
    model = Sequential()
    model.add(LSTM(4, input_dim=vista_atras))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam')
    model.fit(trainX, trainY, nb_epoch=5, batch_size=1, verbose=2)
    # make predictions
    trainPredict = model.predict(trainX)
    testPredict = model.predict(testX)
    # invert predictions
    trainPredict = MinMaxScaler(feature_range=(0, 1)).inverse_transform(trainPredict)
    trainY = MinMaxScaler(feature_range=(0, 1)).inverse_transform([trainY])
    testPredict = MinMaxScaler(feature_range=(0, 1)).inverse_transform(testPredict)
    testY = MinMaxScaler(feature_range=(0, 1)).inverse_transform([testY])
    # calculate root mean squared error
    trainScore = mt.sqrt(mean_squared_error(trainY[0], trainPredict[:,0]))
    print('Train Score: %.2f RMSE' % (trainScore))
    testScore = mt.sqrt(mean_squared_error(testY[0], testPredict[:,0]))
    print('Test Score: %.2f RMSE' % (testScore))
    # shift train predictions for plotting
    trainPredictPlot = np.empty_like(change)
    trainPredictPlot[:, :] = np.nan
    trainPredictPlot[vista_atras:len(trainPredict)+vista_atras, :] = trainPredict
    # shift test predictions for plotting
    testPredictPlot = np.empty_like(change)
    testPredictPlot[:, :] = np.nan
    testPredictPlot[len(trainPredict)+(vista_atras*2)+1:len(change)-1, :] = testPredict
    # plot baseline and predictions
    plt.plot(scaler.inverse_transform(change))
    plt.plot(trainPredictPlot)
    plt.plot(testPredictPlot)
    plt.show()


def main():
    turnos_vista = 1;
    change, real = loadData()
    entrenamiento, test = traning_test(change)
    entrenamientoX, entrenamientoY = crearDataset(entrenamiento, turnos_vista)
    testX, testY = crearDataset(test, turnos_vista)
    # reshape input to be [samples, time steps, features]
    entrenamientoX = np.reshape(entrenamientoX, (entrenamientoX.shape[0], 1, entrenamientoX.shape[1]))
    testX = np.reshape(testX, (testX.shape[0], 1, testX.shape[1]))
    lstm(entrenamientoX, entrenamientoY, testX, testY, change, turnos_vista)


if __name__ == '__main__':
    main()