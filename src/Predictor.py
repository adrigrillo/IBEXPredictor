#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pylab as plt
from matplotlib.pylab import rcParams
from statsmodels.tsa.arima_model import ARIMA

rcParams['figure.figsize'] = 15, 6


def readData():
    """
    Metodo que lee los datos para posteriormente poder usarlos, cambia la fecha de
    texto a datetime
    :return:
    """
    transFecha = lambda fecha: pd.datetime.strptime(fecha, '%Y-%m-%d')
    data = pd.read_csv('../data/Ibex35Normal', parse_dates=[0], index_col=0, date_parser=transFecha, usecols=[0,6])
    timeSerie = pd.DataFrame(data)     #Convierte la tabla en un dataframe para acceder mejor a los datos
    plt.plot(timeSerie["2016"])
    #plt.show()
    return timeSerie["2016"]


def comprobar_estacionalidad(timeSerie):

    #Determing rolling statistics
    rolmean = timeSerie.rolling(window=5, center=False).mean()
    rolstd = timeSerie.rolling(window=5, center=False).std()

    #Plot rolling statistics:
    orig = plt.plot(timeSerie, color='blue',label='Original')
    mean = plt.plot(rolmean, color='red', label='Rolling Mean')
    std = plt.plot(rolstd, color='black', label = 'Rolling Std')
    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation')
    plt.show()


def models(ts):
    ts_log = np.log(ts)
    ts_log_diff = ts_log - ts_log.shift()
    model = ARIMA(ts_log, order=(1, 0, 1))
    results_AR = model.fit(disp=-1)
    plt.plot(ts_log_diff)
    plt.plot(results_AR.fittedvalues, color='red')
    plt.show()


serie = readData()
#comprobar_estacionalidad(serie)
models(serie)