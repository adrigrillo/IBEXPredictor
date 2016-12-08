#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import quandl
import pandas as pd
from builtins import print

quandl.ApiConfig.api_key = 'zxkqftXuQ9RAbjWsw_E2'


def getIBEX35(type):
    if type == 'normal' or type == 'all':
        data = quandl.get('YAHOO/INDEX_IBEX', start_date='2005-01-01', collapse='daily')
        data.to_csv(path_or_buf='../data/Ibex35Normal', sep=',')
    if type == 'change' or type == 'all':
        data = quandl.get('YAHOO/INDEX_IBEX', start_date='2005-01-01', collapse='daily', transform="diff")
        data.to_csv(path_or_buf='../data/Ibex35Change', sep=',')
    if type == 'rchange' or type == 'all':
        data = quandl.get('YAHOO/INDEX_IBEX', start_date='2005-01-01', collapse='daily', transform="rdiff")
        data.to_csv(path_or_buf='../data/Ibex35RChange', sep=',')
    if type == 'normalize' or type == 'all':
        data = quandl.get('YAHOO/INDEX_IBEX', start_date='2005-01-01', collapse='daily', transform="normalize")
        data.to_csv(path_or_buf='../data/Ibex35Normalize', sep=',')
    print('Ibex35 done')


def getDowJones(type):
    if type == 'normal' or type == 'all':
        data = quandl.get('YAHOO/INDEX_DJI', start_date='2005-01-01', collapse='daily')
        data.to_csv(path_or_buf='../data/DowJonesNormal', sep=',')
    if type == 'change' or type == 'all':
        data = quandl.get('YAHOO/INDEX_DJI', start_date='2005-01-01', collapse='daily', transform="diff")
        data.to_csv(path_or_buf='../data/DowJonesChange', sep=',')
    if type == 'rchange' or type == 'all':
        data = quandl.get('YAHOO/INDEX_DJI', start_date='2005-01-01', collapse='daily', transform="rdiff")
        data.to_csv(path_or_buf='../data/DowJonesRChange', sep=',')
    if type == 'normalize' or type == 'all':
        data = quandl.get('YAHOO/INDEX_DJI', start_date='2005-01-01', collapse='daily', transform="normalize")
        data.to_csv(path_or_buf='../data/DowJonesNormalize', sep=',')
    print('Dow Jones done')


def getNikkei(type):
    if type == 'normal' or type == 'all':
        data = quandl.get('YAHOO/INDEX_N225', start_date='2005-01-01', collapse='daily')
        data.to_csv(path_or_buf='../data/NikkeiNormal', sep=',')
    if type == 'change' or type == 'all':
        data = quandl.get('YAHOO/INDEX_N225', start_date='2005-01-01', collapse='daily', transform="diff")
        data.to_csv(path_or_buf='../data/NikkeiChange', sep=',')
    if type == 'rchange' or type == 'all':
        data = quandl.get('YAHOO/INDEX_N225', start_date='2005-01-01', collapse='daily', transform="rdiff")
        data.to_csv(path_or_buf='../data/NikkeiRChange', sep=',')
    if type == 'normalize' or type == 'all':
        data = quandl.get('YAHOO/INDEX_N225', start_date='2005-01-01', collapse='daily', transform="normalize")
        data.to_csv(path_or_buf='../data/NikkeiNormalize', sep=',')
    print('Nikkei done')


def getEuroStock(type):
    if type == 'normal' or type == 'all':
        data = quandl.get('YAHOO/INDEX_STOXX50E', start_date='2005-01-01', collapse='daily')
        data.to_csv(path_or_buf='../data/EuroStockNormal', sep=',')
    if type == 'change' or type == 'all':
        data = quandl.get('YAHOO/INDEX_STOXX50E', start_date='2005-01-01', collapse='daily', transform="diff")
        data.to_csv(path_or_buf='../data/EuroStockChange', sep=',')
    if type == 'rchange' or type == 'all':
        data = quandl.get('YAHOO/INDEX_STOXX50E', start_date='2005-01-01', collapse='daily', transform="rdiff")
        data.to_csv(path_or_buf='../data/EuroStockRChange', sep=',')
    if type == 'normalize' or type == 'all':
        data = quandl.get('YAHOO/INDEX_STOXX50E', start_date='2005-01-01', collapse='daily', transform="normalize")
        data.to_csv(path_or_buf='../data/EuroStockNormalize', sep=',')
    print('LondonStock done')


def getGermanyStock(type):
    if type == 'normal' or type == 'all':
        data = quandl.get('YAHOO/INDEX_GDAXI', start_date='2005-01-01', collapse='daily')
        data.to_csv(path_or_buf='../data/GermanyStockNormal', sep=',')
    if type == 'change' or type == 'all':
        data = quandl.get('YAHOO/INDEX_GDAXI', start_date='2005-01-01', collapse='daily', transform="diff")
        data.to_csv(path_or_buf='../data/GermanyStockChange', sep=',')
    if type == 'rchange' or type == 'all':
        data = quandl.get('YAHOO/INDEX_GDAXI', start_date='2005-01-01', collapse='daily', transform="rdiff")
        data.to_csv(path_or_buf='../data/GermanyStockRChange', sep=',')
    if type == 'normalize' or type == 'all':
        data = quandl.get('YAHOO/INDEX_GDAXI', start_date='2005-01-01', collapse='daily', transform="normalize")
        data.to_csv(path_or_buf='../data/GermanyStockNormalize', sep=',')
    print('GermanyStock done')


def getFranceStock(type):
    if type == 'normal' or type == 'all':
        data = quandl.get('YAHOO/INDEX_FCHI', start_date='2005-01-01', collapse='daily')
        data.to_csv(path_or_buf='../data/FranceStockNormal', sep=',')
    if type == 'change' or type == 'all':
        data = quandl.get('YAHOO/INDEX_FCHI', start_date='2005-01-01', collapse='daily', transform="diff")
        data.to_csv(path_or_buf='../data/FranceStockChange', sep=',')
    if type == 'rchange' or type == 'all':
        data = quandl.get('YAHOO/INDEX_FCHI', start_date='2005-01-01', collapse='daily', transform="rdiff")
        data.to_csv(path_or_buf='../data/FranceStockRChange', sep=',')
    if type == 'normalize' or type == 'all':
        data = quandl.get('YAHOO/INDEX_FCHI', start_date='2005-01-01', collapse='daily', transform="normalize")
        data.to_csv(path_or_buf='../data/FranceStockRChange', sep=',')
    print('FranceStock done')


def getAll(type):
    if type == 'normal' or type == 'all':
        data = quandl.get(['YAHOO/INDEX_IBEX.4', 'YAHOO/INDEX_DJI.4', 'YAHOO/INDEX_STOXX50E.4', 'YAHOO/INDEX_N225.4',
                           'YAHOO/INDEX_FCHI.4', 'YAHOO/INDEX_GDAXI.4', 'YAHOO/INDEX_IBEX.4'], start_date='2005-01-01',
                          collapse='daily')
        data.to_csv(path_or_buf='../data/AllNormal', sep=',')
    if type == 'change' or type == 'all':
        data = quandl.get(['YAHOO/INDEX_IBEX.4', 'YAHOO/INDEX_DJI.4', 'YAHOO/INDEX_STOXX50E.4', 'YAHOO/INDEX_N225.4',
                           'YAHOO/INDEX_FCHI.4', 'YAHOO/INDEX_GDAXI.4', 'YAHOO/INDEX_IBEX.4'], start_date='2005-01-01',
                          collapse='daily', transform="diff")
        data.to_csv(path_or_buf='../data/AllChange', sep=',')
    if type == 'rchange' or type == 'all':
        data = quandl.get(['YAHOO/INDEX_IBEX.4', 'YAHOO/INDEX_DJI.4', 'YAHOO/INDEX_STOXX50E.4', 'YAHOO/INDEX_N225.4',
                           'YAHOO/INDEX_FCHI.4', 'YAHOO/INDEX_GDAXI.4', 'YAHOO/INDEX_IBEX.4'], start_date='2005-01-01',
                          collapse='daily', transform="rdiff")
        data.to_csv(path_or_buf='../data/AllRChange', sep=',')
    if type == 'normalize' or type == 'all':
        data = quandl.get(['YAHOO/INDEX_IBEX.4', 'YAHOO/INDEX_DJI.4', 'YAHOO/INDEX_STOXX50E.4', 'YAHOO/INDEX_N225.4',
                           'YAHOO/INDEX_FCHI.4', 'YAHOO/INDEX_GDAXI.4', 'YAHOO/INDEX_IBEX.4'], start_date='2005-01-01',
                          collapse='daily', transform="normalize")
        data.to_csv(path_or_buf='../data/AllNormalize', sep=',')
    print('All in one done')


def closeAll(type):
    """ Metodo que creara dos csv, uno con los datos de cierre de las bolsas a estudiar y otro con los resultados
        del ibex de ese mismo dia, que posteriomente correremos una posicion para tomarlo como prediccion
    :param type: Los tipos de datos a obtener, ya sean valores normales o cambio
    :return: csv con los datos
    """
    """ Guardamos los datos de cierre del ibex, que es nuestro oobjetivo """
    next_day = quandl.get('YAHOO/INDEX_IBEX.4', start_date='2000-01-01', collapse='daily', transform='diff')
    next_day.to_csv(path_or_buf='../data/NextDay', sep=',')
    """ Guardamos los datos de cierre de las demas bolsas de estudio """
    if type == 'normal' or type == 'all':
        data = quandl.get(['YAHOO/INDEX_IBEX.4', 'YAHOO/INDEX_DJI.4', 'YAHOO/INDEX_STOXX50E.4', 'YAHOO/INDEX_N225.4',
                           'YAHOO/INDEX_FCHI.4', 'YAHOO/INDEX_GDAXI.4'], start_date='2000-01-01', collapse='daily')
        data.to_csv(path_or_buf='../data/CloseNormal', sep=',')
    if type == 'change' or type == 'all':
        data = quandl.get(['YAHOO/INDEX_IBEX.4', 'YAHOO/INDEX_DJI.4', 'YAHOO/INDEX_STOXX50E.4', 'YAHOO/INDEX_N225.4',
                           'YAHOO/INDEX_FCHI.4', 'YAHOO/INDEX_GDAXI.4'], start_date='2000-01-01',
                          collapse='daily', transform="diff")
        data.to_csv(path_or_buf='../data/CloseChange', sep=',')
    if type == 'rchange' or type == 'all':
        data = quandl.get(['YAHOO/INDEX_IBEX.4', 'YAHOO/INDEX_DJI.4', 'YAHOO/INDEX_STOXX50E.4', 'YAHOO/INDEX_N225.4',
                           'YAHOO/INDEX_FCHI.4', 'YAHOO/INDEX_GDAXI.4'], start_date='2000-01-01',
                          collapse='daily', transform="rdiff")
        data.to_csv(path_or_buf='../data/CloseRChange', sep=',')
    if type == 'normalize' or type == 'all':
        data = quandl.get(['YAHOO/INDEX_IBEX.4', 'YAHOO/INDEX_DJI.4', 'YAHOO/INDEX_STOXX50E.4', 'YAHOO/INDEX_N225.4',
                           'YAHOO/INDEX_FCHI.4', 'YAHOO/INDEX_GDAXI.4'], start_date='2000-01-01',
                          collapse='daily', transform="normalize")
        data.to_csv(path_or_buf='../data/CloseNormalize', sep=',')
    print('Closing done')


def final_data_creator(type):
    """
    Este metodo cambiara los resultados de los datos del dia siguiente a 1 si sube y 0 si baja o se mantiene igual
    que el dia anterior. Ademas une las predicciones a los datos anteriores
    :param type:
    :return:
    """
    next_day = pd.read_csv('../data/NextDay', index_col='Date', parse_dates=True, na_values=['nan'])
    """ Cambiamos los resultados por 1 si sube y 0 si baja """
    next_day.loc[next_day['Close'] > 0, 'Close'] = 1
    next_day.loc[next_day['Close'] <= 0, 'Close'] = 0
    """ Subimos los resultados un dia para que pasen a ser predicciones del dia siguiente """
    next_day.Close = next_day.Close.shift(-1)
    if type == 'normal' or type == 'all':
        closings = pd.read_csv('../data/CloseNormal', index_col='Date', parse_dates=True, na_values=['nan'])
        closings = closings.join(next_day)
        """ Con esto eliminamos los datos de los dias en los que el ibex no opera """
        closings = closings.dropna(subset=['Close'])
        """ Si algun mercado secundario no abre un dia se rellenan sus datos con el dia anterior para la prediccion """
        closings.fillna(method='ffill', inplace="TRUE")
        closings.fillna(method='bfill', inplace="TRUE")
        """ Guardamos """
        closings.to_csv(path_or_buf='../data/ProcessedNormal.csv', sep=',')
    if type == 'change' or type == 'all':
        closings = pd.read_csv('../data/CloseChange', index_col='Date', parse_dates=True, na_values=['nan'])
        closings = closings.join(next_day)
        """ Con esto eliminamos los datos de los dias en los que el ibex no opera """
        closings = closings.dropna(subset=['Close'])
        """ Si algun mercado secundario no abre un dia se rellenan sus datos con el dia anterior para la prediccion """
        closings.fillna(method='ffill', inplace="TRUE")
        closings.fillna(method='bfill', inplace="TRUE")
        """ Guardamos """
        closings.to_csv(path_or_buf='../data/ProcessedChange.csv', sep=',')
    if type == 'rchange' or type == 'all':
        closings = pd.read_csv('../data/CloseRChange', index_col='Date', parse_dates=True, na_values=['nan'])
        closings = closings.join(next_day)
        """ Con esto eliminamos los datos de los dias en los que el ibex no opera """
        closings = closings.dropna(subset=['Close'])
        """ Si algun mercado secundario no abre un dia se rellenan sus datos con el dia anterior para la prediccion """
        closings.fillna(method='ffill', inplace="TRUE")
        closings.fillna(method='bfill', inplace="TRUE")
        """ Guardamos """
        closings.to_csv(path_or_buf='../data/ProcessedRChange.csv', sep=',')
    if type == 'normalize' or type == 'all':
        closings = pd.read_csv('../data/CloseNormalize', index_col='Date', parse_dates=True, na_values=['nan'])
        closings = closings.join(next_day)
        """ Con esto eliminamos los datos de los dias en los que el ibex no opera """
        closings = closings.dropna(subset=['Close'])
        """ Si algun mercado secundario no abre un dia se rellenan sus datos con el dia anterior para la prediccion """
        closings.fillna(method='ffill', inplace="TRUE")
        closings.fillna(method='bfill', inplace="TRUE")
        """ Guardamos """
        closings.to_csv(path_or_buf='../data/ProcessedNormalized.csv', sep=',')
    print('Data processing done')


def five_final_data_creator(type):
    """
    Este metodo cambiara los resultados de los datos del dia siguiente a 1 si sube y 0 si baja o se mantiene igual
    que el dia anterior tomando los datos de los 5 dias anteriores Ademas une las predicciones a los datos anteriores
    :param type:
    :return:
    """
    next_day = pd.read_csv('../data/NextDay', index_col='Date', parse_dates=True, na_values=['nan'])
    """ Cambiamos los resultados por 1 si sube y 0 si baja """
    next_day.loc[next_day['Close'] > 0, 'Close'] = 1
    next_day.loc[next_day['Close'] <= 0, 'Close'] = 0
    """ Subimos los resultados un dia para que pasen a ser predicciones del dia siguiente """
    next_day.Close = next_day.Close.shift(-5)
    if type == 'normal' or type == 'all':
        closings = pd.read_csv('../data/CloseNormal', index_col='Date', parse_dates=True, na_values=['nan'])
        """ Empezamos con los 5 dias """
        closings = closings.rename(columns={'YAHOO/INDEX_IBEX - Close':'Ibex', 'YAHOO/INDEX_DJI - Close':'DowJones',
                                            'YAHOO/INDEX_STOXX50E - Close':'Stoxx', 'YAHOO/INDEX_N225 - Close':'Nikkei',
                                            'YAHOO/INDEX_FCHI - Close':'Francia',
                                            'YAHOO/INDEX_GDAXI - Close':'Alemania'})
        to_take = closings
        """ 5 DIA """
        closings = to_take.rename(columns={'Ibex':'Ibex5', 'DowJones':'DowJones5', 'Stoxx':'Stoxx5',
                                            'Nikkei':'Nikkei5', 'Francia':'Francia5', 'Alemania':'Alemania5'})
        """ 4 DIA subimos los valores un dia """
        closings4 = to_take.rename(columns={'Ibex':'Ibex4', 'DowJones':'DowJones4', 'Stoxx':'Stoxx4',
                                            'Nikkei':'Nikkei4', 'Francia':'Francia4', 'Alemania':'Alemania4'})
        closings4.Ibex4 = closings4.Ibex4.shift(-1)
        closings4.DowJones4 = closings4.DowJones4.shift(-1)
        closings4.Stoxx4 = closings4.Stoxx4.shift(-1)
        closings4.Nikkei4 = closings4.Nikkei4.shift(-1)
        closings4.Francia4 = closings4.Francia4.shift(-1)
        closings4.Alemania4 = closings4.Alemania4.shift(-1)
        closings = closings.join(closings4)
        """ 3 DIA subimos dos"""
        closings3 = to_take.rename(columns={'Ibex':'Ibex3', 'DowJones':'DowJones3', 'Stoxx':'Stoxx3',
                                             'Nikkei':'Nikkei3', 'Francia':'Francia3', 'Alemania':'Alemania3'})
        closings3.Ibex3 = closings3.Ibex3.shift(-2)
        closings3.DowJones3 = closings3.DowJones3.shift(-2)
        closings3.Stoxx3 = closings3.Stoxx3.shift(-2)
        closings3.Nikkei3 = closings3.Nikkei3.shift(-2)
        closings3.Francia3 = closings3.Francia3.shift(-2)
        closings3.Alemania3 = closings3.Alemania3.shift(-2)
        closings = closings.join(closings3)
        """ 2 DIA subimos dos"""
        closings2 = to_take.rename(columns={'Ibex':'Ibex2', 'DowJones':'DowJones2', 'Stoxx':'Stoxx2',
                                             'Nikkei':'Nikkei2', 'Francia':'Francia2', 'Alemania':'Alemania2'})
        closings2.Ibex2 = closings2.Ibex2.shift(-3)
        closings2.DowJones2 = closings2.DowJones2.shift(-3)
        closings2.Stoxx2 = closings2.Stoxx2.shift(-3)
        closings2.Nikkei2 = closings2.Nikkei2.shift(-3)
        closings2.Francia2 = closings2.Francia2.shift(-3)
        closings2.Alemania2 = closings2.Alemania2.shift(-3)
        closings = closings.join(closings2)
        """ 1 DIA subimos dos"""
        closings1 = to_take.rename(columns={'Ibex':'Ibex1', 'DowJones':'DowJones1', 'Stoxx':'Stoxx1',
                                             'Nikkei':'Nikkei1', 'Francia':'Francia1', 'Alemania':'Alemania1'})
        closings1.Ibex1 = closings1.Ibex1.shift(-4)
        closings1.DowJones1 = closings1.DowJones1.shift(-4)
        closings1.Stoxx1 = closings1.Stoxx1.shift(-4)
        closings1.Nikkei1 = closings1.Nikkei1.shift(-4)
        closings1.Francia1 = closings1.Francia1.shift(-4)
        closings1.Alemania1 = closings1.Alemania1.shift(-4)
        closings = closings.join(closings1)
        """ Añadimos la prediccion """
        closings = closings.join(next_day)
        """ Con esto eliminamos los datos de los dias en los que el ibex no opera """
        closings = closings.dropna(subset=['Close'])
        """ Si algun mercado secundario no abre un dia se rellenan sus datos con el dia anterior para la prediccion """
        closings.fillna(method='ffill', inplace="TRUE")
        closings.fillna(method='bfill', inplace="TRUE")
        """ Guardamos """
        closings.to_csv(path_or_buf='../data/5DayNormal.csv', sep=',')
    if type == 'change' or type == 'all':
        closings = pd.read_csv('../data/CloseChange', index_col='Date', parse_dates=True, na_values=['nan'])
        """ Empezamos con los 5 dias """
        closings = closings.rename(columns={'YAHOO/INDEX_IBEX - Close':'Ibex', 'YAHOO/INDEX_DJI - Close':'DowJones',
                                            'YAHOO/INDEX_STOXX50E - Close':'Stoxx', 'YAHOO/INDEX_N225 - Close':'Nikkei',
                                            'YAHOO/INDEX_FCHI - Close':'Francia',
                                            'YAHOO/INDEX_GDAXI - Close':'Alemania'})
        to_take = closings
        """ 5 DIA """
        closings = to_take.rename(columns={'Ibex':'Ibex5', 'DowJones':'DowJones5', 'Stoxx':'Stoxx5',
                                           'Nikkei':'Nikkei5', 'Francia':'Francia5', 'Alemania':'Alemania5'})
        """ 4 DIA subimos los valores un dia """
        closings4 = to_take.rename(columns={'Ibex':'Ibex4', 'DowJones':'DowJones4', 'Stoxx':'Stoxx4',
                                            'Nikkei':'Nikkei4', 'Francia':'Francia4', 'Alemania':'Alemania4'})
        closings4.Ibex4 = closings4.Ibex4.shift(-1)
        closings4.DowJones4 = closings4.DowJones4.shift(-1)
        closings4.Stoxx4 = closings4.Stoxx4.shift(-1)
        closings4.Nikkei4 = closings4.Nikkei4.shift(-1)
        closings4.Francia4 = closings4.Francia4.shift(-1)
        closings4.Alemania4 = closings4.Alemania4.shift(-1)
        closings = closings.join(closings4)
        """ 3 DIA subimos dos"""
        closings3 = to_take.rename(columns={'Ibex':'Ibex3', 'DowJones':'DowJones3', 'Stoxx':'Stoxx3',
                                            'Nikkei':'Nikkei3', 'Francia':'Francia3', 'Alemania':'Alemania3'})
        closings3.Ibex3 = closings3.Ibex3.shift(-2)
        closings3.DowJones3 = closings3.DowJones3.shift(-2)
        closings3.Stoxx3 = closings3.Stoxx3.shift(-2)
        closings3.Nikkei3 = closings3.Nikkei3.shift(-2)
        closings3.Francia3 = closings3.Francia3.shift(-2)
        closings3.Alemania3 = closings3.Alemania3.shift(-2)
        closings = closings.join(closings3)
        """ 2 DIA subimos dos"""
        closings2 = to_take.rename(columns={'Ibex':'Ibex2', 'DowJones':'DowJones2', 'Stoxx':'Stoxx2',
                                            'Nikkei':'Nikkei2', 'Francia':'Francia2', 'Alemania':'Alemania2'})
        closings2.Ibex2 = closings2.Ibex2.shift(-3)
        closings2.DowJones2 = closings2.DowJones2.shift(-3)
        closings2.Stoxx2 = closings2.Stoxx2.shift(-3)
        closings2.Nikkei2 = closings2.Nikkei2.shift(-3)
        closings2.Francia2 = closings2.Francia2.shift(-3)
        closings2.Alemania2 = closings2.Alemania2.shift(-3)
        closings = closings.join(closings2)
        """ 1 DIA subimos dos"""
        closings1 = to_take.rename(columns={'Ibex':'Ibex1', 'DowJones':'DowJones1', 'Stoxx':'Stoxx1',
                                            'Nikkei':'Nikkei1', 'Francia':'Francia1', 'Alemania':'Alemania1'})
        closings1.Ibex1 = closings1.Ibex1.shift(-4)
        closings1.DowJones1 = closings1.DowJones1.shift(-4)
        closings1.Stoxx1 = closings1.Stoxx1.shift(-4)
        closings1.Nikkei1 = closings1.Nikkei1.shift(-4)
        closings1.Francia1 = closings1.Francia1.shift(-4)
        closings1.Alemania1 = closings1.Alemania1.shift(-4)
        closings = closings.join(closings1)
        """ Añadimos la prediccion """
        closings = closings.join(next_day)
        """ Con esto eliminamos los datos de los dias en los que el ibex no opera """
        closings = closings.dropna(subset=['Close'])
        """ Si algun mercado secundario no abre un dia se rellenan sus datos con el dia anterior para la prediccion """
        closings.fillna(method='ffill', inplace="TRUE")
        closings.fillna(method='bfill', inplace="TRUE")
        """ Guardamos """
        closings.to_csv(path_or_buf='../data/5DayChange.csv', sep=',')
    if type == 'rchange' or type == 'all':
        closings = pd.read_csv('../data/CloseRChange', index_col='Date', parse_dates=True, na_values=['nan'])
        """ Empezamos con los 5 dias """
        closings = closings.rename(columns={'YAHOO/INDEX_IBEX - Close':'Ibex', 'YAHOO/INDEX_DJI - Close':'DowJones',
                                            'YAHOO/INDEX_STOXX50E - Close':'Stoxx', 'YAHOO/INDEX_N225 - Close':'Nikkei',
                                            'YAHOO/INDEX_FCHI - Close':'Francia',
                                            'YAHOO/INDEX_GDAXI - Close':'Alemania'})
        to_take = closings
        """ 5 DIA """
        closings = to_take.rename(columns={'Ibex':'Ibex5', 'DowJones':'DowJones5', 'Stoxx':'Stoxx5',
                                           'Nikkei':'Nikkei5', 'Francia':'Francia5', 'Alemania':'Alemania5'})
        """ 4 DIA subimos los valores un dia """
        closings4 = to_take.rename(columns={'Ibex':'Ibex4', 'DowJones':'DowJones4', 'Stoxx':'Stoxx4',
                                            'Nikkei':'Nikkei4', 'Francia':'Francia4', 'Alemania':'Alemania4'})
        closings4.Ibex4 = closings4.Ibex4.shift(-1)
        closings4.DowJones4 = closings4.DowJones4.shift(-1)
        closings4.Stoxx4 = closings4.Stoxx4.shift(-1)
        closings4.Nikkei4 = closings4.Nikkei4.shift(-1)
        closings4.Francia4 = closings4.Francia4.shift(-1)
        closings4.Alemania4 = closings4.Alemania4.shift(-1)
        closings = closings.join(closings4)
        """ 3 DIA subimos dos"""
        closings3 = to_take.rename(columns={'Ibex':'Ibex3', 'DowJones':'DowJones3', 'Stoxx':'Stoxx3',
                                            'Nikkei':'Nikkei3', 'Francia':'Francia3', 'Alemania':'Alemania3'})
        closings3.Ibex3 = closings3.Ibex3.shift(-2)
        closings3.DowJones3 = closings3.DowJones3.shift(-2)
        closings3.Stoxx3 = closings3.Stoxx3.shift(-2)
        closings3.Nikkei3 = closings3.Nikkei3.shift(-2)
        closings3.Francia3 = closings3.Francia3.shift(-2)
        closings3.Alemania3 = closings3.Alemania3.shift(-2)
        closings = closings.join(closings3)
        """ 2 DIA subimos dos"""
        closings2 = to_take.rename(columns={'Ibex':'Ibex2', 'DowJones':'DowJones2', 'Stoxx':'Stoxx2',
                                            'Nikkei':'Nikkei2', 'Francia':'Francia2', 'Alemania':'Alemania2'})
        closings2.Ibex2 = closings2.Ibex2.shift(-3)
        closings2.DowJones2 = closings2.DowJones2.shift(-3)
        closings2.Stoxx2 = closings2.Stoxx2.shift(-3)
        closings2.Nikkei2 = closings2.Nikkei2.shift(-3)
        closings2.Francia2 = closings2.Francia2.shift(-3)
        closings2.Alemania2 = closings2.Alemania2.shift(-3)
        closings = closings.join(closings2)
        """ 1 DIA subimos dos"""
        closings1 = to_take.rename(columns={'Ibex':'Ibex1', 'DowJones':'DowJones1', 'Stoxx':'Stoxx1',
                                            'Nikkei':'Nikkei1', 'Francia':'Francia1', 'Alemania':'Alemania1'})
        closings1.Ibex1 = closings1.Ibex1.shift(-4)
        closings1.DowJones1 = closings1.DowJones1.shift(-4)
        closings1.Stoxx1 = closings1.Stoxx1.shift(-4)
        closings1.Nikkei1 = closings1.Nikkei1.shift(-4)
        closings1.Francia1 = closings1.Francia1.shift(-4)
        closings1.Alemania1 = closings1.Alemania1.shift(-4)
        closings = closings.join(closings1)
        """ Añadimos la prediccion """
        closings = closings.join(next_day)
        """ Con esto eliminamos los datos de los dias en los que el ibex no opera """
        closings = closings.dropna(subset=['Close'])
        """ Si algun mercado secundario no abre un dia se rellenan sus datos con el dia anterior para la prediccion """
        closings.fillna(method='ffill', inplace="TRUE")
        closings.fillna(method='bfill', inplace="TRUE")
        """ Guardamos """
        closings.to_csv(path_or_buf='../data/5DayRChange.csv', sep=',')
    if type == 'normalize' or type == 'all':
        closings = pd.read_csv('../data/CloseNormalize', index_col='Date', parse_dates=True, na_values=['nan'])
        """ Empezamos con los 5 dias """
        closings = closings.rename(columns={'YAHOO/INDEX_IBEX - Close':'Ibex', 'YAHOO/INDEX_DJI - Close':'DowJones',
                                            'YAHOO/INDEX_STOXX50E - Close':'Stoxx', 'YAHOO/INDEX_N225 - Close':'Nikkei',
                                            'YAHOO/INDEX_FCHI - Close':'Francia',
                                            'YAHOO/INDEX_GDAXI - Close':'Alemania'})
        to_take = closings
        """ 5 DIA """
        closings = to_take.rename(columns={'Ibex':'Ibex5', 'DowJones':'DowJones5', 'Stoxx':'Stoxx5',
                                           'Nikkei':'Nikkei5', 'Francia':'Francia5', 'Alemania':'Alemania5'})
        """ 4 DIA subimos los valores un dia """
        closings4 = to_take.rename(columns={'Ibex':'Ibex4', 'DowJones':'DowJones4', 'Stoxx':'Stoxx4',
                                            'Nikkei':'Nikkei4', 'Francia':'Francia4', 'Alemania':'Alemania4'})
        closings4.Ibex4 = closings4.Ibex4.shift(-1)
        closings4.DowJones4 = closings4.DowJones4.shift(-1)
        closings4.Stoxx4 = closings4.Stoxx4.shift(-1)
        closings4.Nikkei4 = closings4.Nikkei4.shift(-1)
        closings4.Francia4 = closings4.Francia4.shift(-1)
        closings4.Alemania4 = closings4.Alemania4.shift(-1)
        closings = closings.join(closings4)
        """ 3 DIA subimos dos"""
        closings3 = to_take.rename(columns={'Ibex':'Ibex3', 'DowJones':'DowJones3', 'Stoxx':'Stoxx3',
                                            'Nikkei':'Nikkei3', 'Francia':'Francia3', 'Alemania':'Alemania3'})
        closings3.Ibex3 = closings3.Ibex3.shift(-2)
        closings3.DowJones3 = closings3.DowJones3.shift(-2)
        closings3.Stoxx3 = closings3.Stoxx3.shift(-2)
        closings3.Nikkei3 = closings3.Nikkei3.shift(-2)
        closings3.Francia3 = closings3.Francia3.shift(-2)
        closings3.Alemania3 = closings3.Alemania3.shift(-2)
        closings = closings.join(closings3)
        """ 2 DIA subimos dos"""
        closings2 = to_take.rename(columns={'Ibex':'Ibex2', 'DowJones':'DowJones2', 'Stoxx':'Stoxx2',
                                            'Nikkei':'Nikkei2', 'Francia':'Francia2', 'Alemania':'Alemania2'})
        closings2.Ibex2 = closings2.Ibex2.shift(-3)
        closings2.DowJones2 = closings2.DowJones2.shift(-3)
        closings2.Stoxx2 = closings2.Stoxx2.shift(-3)
        closings2.Nikkei2 = closings2.Nikkei2.shift(-3)
        closings2.Francia2 = closings2.Francia2.shift(-3)
        closings2.Alemania2 = closings2.Alemania2.shift(-3)
        closings = closings.join(closings2)
        """ 1 DIA subimos dos"""
        closings1 = to_take.rename(columns={'Ibex':'Ibex1', 'DowJones':'DowJones1', 'Stoxx':'Stoxx1',
                                            'Nikkei':'Nikkei1', 'Francia':'Francia1', 'Alemania':'Alemania1'})
        closings1.Ibex1 = closings1.Ibex1.shift(-4)
        closings1.DowJones1 = closings1.DowJones1.shift(-4)
        closings1.Stoxx1 = closings1.Stoxx1.shift(-4)
        closings1.Nikkei1 = closings1.Nikkei1.shift(-4)
        closings1.Francia1 = closings1.Francia1.shift(-4)
        closings1.Alemania1 = closings1.Alemania1.shift(-4)
        closings = closings.join(closings1)
        """ Añadimos la prediccion """
        closings = closings.join(next_day)
        """ Con esto eliminamos los datos de los dias en los que el ibex no opera """
        closings = closings.dropna(subset=['Close'])
        """ Si algun mercado secundario no abre un dia se rellenan sus datos con el dia anterior para la prediccion """
        closings.fillna(method='ffill', inplace="TRUE")
        closings.fillna(method='bfill', inplace="TRUE")
        """ Guardamos """
        closings.to_csv(path_or_buf='../data/5DayNormalized.csv', sep=',')
    print('Data processing done')


def main():
    """getIBEX35('all')
    getDowJones('all')
    getNikkei('all')
    getEuroStock('all')
    getGermanyStock('all')
    getFranceStock('all')
    getAll('all')
    closeAll('all')
    final_data_creator('all')"""
    five_final_data_creator('all')


if __name__ == '__main__':
    main()