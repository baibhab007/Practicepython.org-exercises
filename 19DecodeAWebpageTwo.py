import requests
r = requests.get('http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture')
print(r.text)
