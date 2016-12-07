#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib as plt

def plot_data(data):
    data.plot()
    plt.show()


def main():
    """
    Aqui obtenemos los datos y llamamos a la representacion
    :return: representacion de la grafica
    """
    raiz = '../data'
    fichero = 'ProcesedNorm'
    pd.read_csv('../data/Processed')


if __name__ == '__main__':
    main()
