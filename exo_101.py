from http.client import HTTPConnection
connex=HTTPConnection("google.com")
conn=connex.getresponse()
contenu=conn.read()
print(contenu)