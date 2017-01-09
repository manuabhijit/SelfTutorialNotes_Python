import urllib

goog_url = "http://real-chart.finance.yahoo.com/table.csv?s=GOOG&d=5&e=12&f=2016&g=d&a=7&b=19&c=2004&ignore=.csv"

def stocks(csv_url):
    response = urllib.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url = r'goog.csv'


    fx = open (dest_url, "w")
    for line in lines:
        fx.write(line + "\n")

    fx.close()

stocks(goog_url)

fr = open('goog.csv', 'r')
text = fr.read()
print text
fr.close()