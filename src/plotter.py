#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

def plot_data(data):
    data.plot()
    plt.show()


def main():
    """
    Aqui obtenemos los datos y llamamos a la representacion
    :return: representacion de la grafica
    """
    raiz = '../data/'
    fichero = 'ProcessedNormalized.csv'
    data = pd.read_csv(filepath_or_buffer=raiz+fichero, index_col='Date', parse_dates=True)
    plot_data(data)


if __name__ == '__main__':
    main()
