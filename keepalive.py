import re
import requests
import os
import time

URL = 'http://192.168.211.3'


while (True):
    reponse = requests.get(URL)
    pattern = re.compile('<title>(.*?)</title>', re.S)
    tittle = re.findall(pattern, reponse.text)
    tittle = tittle[0]
    if tittle == '注销页':
        print(tittle)
        time.sleep(5)
        pass
    else:
        os.system("python login.py")