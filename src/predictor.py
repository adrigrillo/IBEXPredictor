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


# convert an array of values into a dataset matrix
def crearDataset(dataset, vista_atras):
    dataX, dataY = [], []
    for i in range(len(dataset)-vista_atras-1):
        a = dataset[i:(i+vista_atras), 0]
        dataX.append(a)
        dataY.append(dataset[i + vista_atras, 0])
    return np.array(dataX), np.array(dataY)


def main():
    transFecha = lambda fecha: pd.datetime.strptime(fecha, '%Y-%m-%d')
    dataReal = pd.read_csv('../data/Ibex35Normal', engine='python', parse_dates=[0], index_col=0,
                            date_parser=transFecha, usecols=[0,6], skipfooter=3)
    adjClose = pd.read_csv('../data/Ibex35Normalize', usecols=[6], engine='python')
    dataChange = adjClose.values
    dataChange = dataChange.astype('float32')
    scaler = MinMaxScaler(feature_range=(0, 1))
    dataNorm = scaler.fit_transform(dataChange)

    train_size = int(len(dataNorm) * 0.9)
    train, test = dataNorm[0:train_size, :], dataNorm[train_size:len(dataNorm), :]
    print("Conjunto de entrenamiento, longitud: ", len(train))
    print("Conjunto de test, longitud: ",  len(test))

    turnos_vista = 3
    trainX, trainY = crearDataset(train, turnos_vista)
    testX, testY = crearDataset(test, turnos_vista)

    trainX = np.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))
    testX = np.reshape(testX, (testX.shape[0], 1, testX.shape[1]))

    # create and fit the LSTM network
    model = Sequential()
    model.add(LSTM(4, input_dim=turnos_vista))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam')
    model.fit(trainX, trainY, nb_epoch=3, batch_size=1, verbose=2)
    # make predictions
    trainPredict = model.predict(trainX)
    testPredict = model.predict(testX)
    # invert predictions
    trainPredict = scaler.inverse_transform(trainPredict)
    trainY = scaler.inverse_transform([trainY])
    testPredict = scaler.inverse_transform(testPredict)
    testY = scaler.inverse_transform([testY])
    # calculate root mean squared error
    trainScore = mt.sqrt(mean_squared_error(trainY[0], trainPredict[:,0]))
    print('Train Score: %.2f RMSE' % (trainScore))
    testScore = mt.sqrt(mean_squared_error(testY[0], testPredict[:,0]))
    print('Test Score: %.2f RMSE' % (testScore))
    # shift train predictions for plotting
    trainPredictPlot = np.empty_like(dataNorm)
    trainPredictPlot[:, :] = np.nan
    trainPredictPlot[turnos_vista:len(trainPredict)+turnos_vista, :] = trainPredict
    # shift test predictions for plotting
    testPredictPlot = np.empty_like(dataNorm)
    testPredictPlot[:, :] = np.nan
    testPredictPlot[len(trainPredict)+(turnos_vista*2)+1:len(dataNorm)-1, :] = testPredict
    # plot baseline and predictions
    plt.plot(scaler.inverse_transform(dataNorm), color='blue', label='Real')
    plt.plot(trainPredictPlot, color='red', label='Entrenamiento')
    plt.plot(testPredictPlot, color='green', label='Test')
    plt.legend(loc='best')
    plt.title('Predicción Ibex35 a un día')
    plt.show()


if __name__ == '__main__':
    main()