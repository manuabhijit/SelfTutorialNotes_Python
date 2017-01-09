import random
import urllib

def test_downloader(url):
    name = random.randrange(2, 2200)
    filename = str(name)+".jpg"
    urllib.urlretrieve(url, filename)

test_downloader("https://scontent.fdel1-1.fna.fbcdn.net/v/t1.0-1/c340.3.465.465/s100x100/12573746_10207338107522963_695592788160241284_n.jpg?oh=5a6940fd6fef0f1d7630e0cb31704b68&oe=57C56C00")