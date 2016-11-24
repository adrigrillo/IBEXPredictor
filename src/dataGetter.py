import quandl
quandl.ApiConfig.api_key = 'zxkqftXuQ9RAbjWsw_E2'


def getIBEX35(type):
    if type == 'normal':
        data = quandl.get('YAHOO/INDEX_IBEX', start_date='2005-01-01', collapse='daily')
        data.to_csv(path_or_buf='../data/Ibex35Normal', sep=',')
    elif type == 'change':
        data = quandl.get('YAHOO/INDEX_IBEX', start_date='2005-01-01', collapse='daily', transform="diff")
        data.to_csv(path_or_buf='../data/Ibex35Change', sep=',')
    elif type == 'rchange':
        data = quandl.get('YAHOO/INDEX_IBEX', start_date='2005-01-01', collapse='daily', transform="rdiff")
        data.to_csv(path_or_buf='../data/Ibex35Change', sep=',')


def main():
    getIBEX35('normal')


if __name__ == '__main__':
    main()