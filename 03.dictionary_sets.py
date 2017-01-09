stocks = {'goog': 520.44, 'fb': 76, 'yhoo': 39.17, 'amzn': 306.21}

print stocks['fb']

for k, v in stocks.items():
    print k + " " + str(stocks[k]) + " "

print "\n\n"

print ("minimum " + str(min(zip(stocks.values(), stocks.keys()))))
print ("maximum " + str(max(zip(stocks.values(), stocks.keys()))))
print ("sorting " + str(sorted(zip(stocks.values(), stocks.keys()))))