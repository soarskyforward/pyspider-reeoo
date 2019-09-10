# 嗯，pyspider还挺好用的
# reeoo.csv     Downloading from pyspider http:www.reeoo.com

import csv
import requests

path = ''   #your own path
lis_name = []
lis_imgurl = []
with open('reeoo_2.csv', encoding = 'utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        img_url = row[2]
        name = row[4]
        lis_name.append(name)
        lis_imgurl.append(img_url)



for (name, img_url) in zip(lis_name[1:],lis_imgurl[1:]):  #lis_name[0] is title
    r = requests.get(img_url)
    with open(path + name + '.jpg','wb') as f:
        f.write(r.content)
