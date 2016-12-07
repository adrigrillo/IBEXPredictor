#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import quandl
import pandas as pd
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
    next_day = quandl.get('YAHOO/INDEX_IBEX.4', start_date='2005-01-01', collapse='daily', transform='diff')
    next_day.to_csv(path_or_buf='../data/NextDay', sep=',')
    """ Guardamos los datos de cierre de las demas bolsas de estudio """
    if type == 'normal' or type == 'all':
        data = quandl.get(['YAHOO/INDEX_IBEX.4', 'YAHOO/INDEX_DJI.4', 'YAHOO/INDEX_STOXX50E.4', 'YAHOO/INDEX_N225.4',
                           'YAHOO/INDEX_FCHI.4', 'YAHOO/INDEX_GDAXI.4'], start_date='2005-01-01', collapse='daily')
        data.to_csv(path_or_buf='../data/CloseNormal', sep=',')
    if type == 'change' or type == 'all':
        data = quandl.get(['YAHOO/INDEX_IBEX.4', 'YAHOO/INDEX_DJI.4', 'YAHOO/INDEX_STOXX50E.4', 'YAHOO/INDEX_N225.4',
                           'YAHOO/INDEX_FCHI.4', 'YAHOO/INDEX_GDAXI.4', 'YAHOO/INDEX_IBEX.4'], start_date='2005-01-01',
                          collapse='daily', transform="diff")
        data.to_csv(path_or_buf='../data/CloseChange', sep=',')
    if type == 'rchange' or type == 'all':
        data = quandl.get(['YAHOO/INDEX_IBEX.4', 'YAHOO/INDEX_DJI.4', 'YAHOO/INDEX_STOXX50E.4', 'YAHOO/INDEX_N225.4',
                           'YAHOO/INDEX_FCHI.4', 'YAHOO/INDEX_GDAXI.4', 'YAHOO/INDEX_IBEX.4'], start_date='2005-01-01',
                          collapse='daily', transform="rdiff")
        data.to_csv(path_or_buf='../data/CloseRChange', sep=',')
    if type == 'normalize' or type == 'all':
        data = quandl.get(['YAHOO/INDEX_IBEX.4', 'YAHOO/INDEX_DJI.4', 'YAHOO/INDEX_STOXX50E.4', 'YAHOO/INDEX_N225.4',
                           'YAHOO/INDEX_FCHI.4', 'YAHOO/INDEX_GDAXI.4', 'YAHOO/INDEX_IBEX.4'], start_date='2005-01-01',
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


def main():
    getIBEX35('all')
    getDowJones('all')
    getNikkei('all')
    getEuroStock('all')
    getGermanyStock('all')
    getFranceStock('all')
    getAll('all')
    closeAll('all')
    final_data_creator('all')


if __name__ == '__main__':
    main()