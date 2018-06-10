import oneforge

client = oneforge.Client('your_api_key')

if client.marketIsOpen() == True:
    print("Market is open!")

print(client.getSymbols())
print(client.getQuotes(['EURUSD', 'GBPJPY']))
print(client.getQuota())
print(client.convert('EUR', 'USD', 100))
