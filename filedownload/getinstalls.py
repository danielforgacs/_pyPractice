import urllib.request


url = 'https://www.python.org/ftp/python/3.5.1'
file_name = 'python-3.5.1.exe'

urllib.request.urlretrieve(url + '/' + file_name, file_name)

