import pandas as pd
import numpy as np
import time
import urllib2

output_dir = '/media/vishal/Share/robots.txt/'

def getrobots(target_url):
    try:
        response = urllib2.urlopen(target_url)
        data = response.read()

        # Write data to file
        filename = output_dir + target_url.split('/')[2]
        file_ = open(filename, 'w')
        file_.write(data)
        file_.close()
    except:
        pass

top_1m = pd.read_csv('./data/top-1m.csv')
top_1m['url'] = 'https://www.' + top_1m['url'].astype(str) + '/robots.txt'


# print(top_1m)

for url in top_1m['url'].tolist():
    print(url)
    getrobots(url)
    time.sleep(0.25)




