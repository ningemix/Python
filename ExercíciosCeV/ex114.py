import urllib.request
try:
    site = urllib.request.urlopen('https://www.pudim.com.br')
except urllib.error.URLError:
    print ('Site Unavailable')
else:
    print ('The site is open')