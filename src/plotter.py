#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

def plot_data(data, title):
    plot = data.plot(title=title)
    plot.set_xlabel("Datos")
    plot.set_ylabel("Fecha")
    plt.show()


def main():
    """
    Aqui obtenemos los datos y llamamos a la representacion
    :return: representacion de la grafica
    """
    raiz = '../data/'
    fichero = 'ProcessedNormal.csv'
    data = pd.read_csv(filepath_or_buffer=raiz+fichero, index_col='Date', parse_dates=True)
    #plot_data(data, "Evolución de las bolsas de 2005-2016")
    data.plot(y='Close')
    plt.show()

if __name__ == '__main__':
    main()
