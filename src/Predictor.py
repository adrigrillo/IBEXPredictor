#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as mpl
from pandas.io.tests.parser import usecols
from sklearn.preprocessing import scale
import tensorflow as tf
import matplotlib.pylab as plt
from matplotlib.pylab import rcParams

rcParams['figure.figsize'] = 15, 6


def realPlot():
    """
    Metodo que dibuja la grafica de los datos reales obtenidos de un documento
    :return: Grafica de los datos
    """
    documento = '../data/mod1'
    A = np.loadtxt(documento, delimiter=',', skiprows=1, usecols=(1, 5))
    A = scale(A)
    #y is the dependent variable
    y = A[:, 1].reshape(-1, 1)
    #A contains the independent variable
    A = A[:, 0].reshape(-1, 1)
    #Plot the high value of the stock price
    mpl.plot(A[:, 0], y[:, 0])
    mpl.show()


def readData():
    """
    Metodo que lee los datos para posteriormente poder usarlos, cambia la fecha de
    texto a datetime
    :return:
    """
    transFecha = lambda fecha: pd.datetime.strptime(fecha, '%Y-%m-%d')
    data = pd.read_csv('../data/Ibex35Normal', parse_dates=[0], index_col=0, date_parser=transFecha, usecols=[0,6])
    dt = pd.DataFrame(data)     #Convierte la tabla en un dataframe para acceder mejor a los datos
    plt.plot(dt)
    plt.show()


readData()