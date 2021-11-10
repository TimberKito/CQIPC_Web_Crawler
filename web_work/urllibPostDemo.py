import urllib.request

req_url = r'https://www.baidu.com'
req_headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
}
res = urllib.request.Request(url=req_url, headers=req_headers)
response = urllib.request.urlopen(res)
html = response.read()
print(html.decode())