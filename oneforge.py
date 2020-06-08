import requests


class Client:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_uri = 'https://api.1forge.com/'   # New API

    def fetch(self, uri):
        fetch_uri = self.base_uri + uri + '&api_key=' + self.api_key
        # print(fetch_uri)
        response = requests.get(fetch_uri)
        return response.json()

    def getQuota(self):
        return self.fetch('quota?cache=false')

    def getSymbols(self):
        return self.fetch('symbols?cache=false')

    def getQuotes(self, pairs):
        return self.fetch('quotes?pairs=' + ','.join(pairs))

    def marketIsOpen(self):
        data = self.fetch('market_status?cache=false')
        try:
            return data['market_is_open']
        except:
            print(data)

    def convert(self, currency_from, currency_to, quantity):
        return self.fetch('convert?from=' + currency_from + '&to=' +
                          currency_to + '&quantity=' + str(quantity))

# End of file
