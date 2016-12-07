import quandl
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

def main():
    """getIBEX35('all')
    getDowJones('all')
    getNikkei('all')
    getEuroStock('all')
    getGermanyStock('all')
    getFranceStock('all')"""
    getAll('all')

if __name__ == '__main__':
    main()