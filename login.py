import requests

url = 'http://10.144.0.3/a70.htm'

data = {
    "DDDDD": 'user_name',
    "upass": 'passwd',
    "R1": "0",
    "R3": "0",
    "R6": "0",
    "pare": "00",
    "0MKKey": "123456",
}
header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja-JP;q=0.6,ja;q=0.5",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Content-Length": "152",
    "Conten-Type": "application/x-www-form-urlencoded",
    "Cookie": "cookie",
    "Host": "10.144.0.3",
    "Origin": "http://10.144.0.3",
    "Referer": "http://10.144.0.3/a70.htm",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}

reponse = requests.post(url, data, headers=header)
print("状态码:", reponse.status_code)
