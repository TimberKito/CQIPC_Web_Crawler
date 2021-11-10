
import urllib.request

url = 'https://www.cnblogs.com/jaolvv'
response = urllib.request.urlopen(url)
print(response.read())