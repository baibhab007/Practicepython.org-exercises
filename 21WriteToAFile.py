import requests
r = requests.get('http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture')
with open('output.txt', 'w') as open_file:
    open_file.write(r.text)
