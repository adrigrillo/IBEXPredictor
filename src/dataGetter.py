import HistoricDataLib.HistoricalQuote_YahooAPI as HistoricalQuote_YahooAPI


def printLines(lst):
    for line in lst:
        print(line)


def printHistoricQuotesYahoo():
    data = HistoricalQuote_YahooAPI.HistoricalQuote()
    printLines(data.GetData('^IBEX', '11-15-2015', '11-18-2016'))


def main():
    printHistoricQuotesYahoo()


if __name__ == '__main__':
    main()