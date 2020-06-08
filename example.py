import oneforge

client = oneforge.Client("your_api_key")

if client.marketIsOpen() is True:
    print("Market is open!")

print(client.getSymbols())
print(client.getQuotes(["EUR/USD", "GBP/JPY"]))
print(client.getQuota())
print(client.convert("EUR", "USD", 100))

# End of file
