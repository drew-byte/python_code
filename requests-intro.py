import requests

#Get 
x = requests.get('http://<target>/get')
print(x.headers)
print(x.headers['Server'])
print(x.status_code)
print(x.elapsed)
print(x.cookies)

#Add a parameter
x = requests.get('http://<target>/get',params={'id':'1'})
print(x.url)

#Add a header with parameter
x = requests.get('http://<target>/get',params={'id':'1'},headers={'Accept':'application/json'})
print(x.text)

#Delete
x = requests.delete('http://<target>/delete')
print(x.text)

#Post
x = requests.post('http://<target>/post',data={'id':'2'})
print(x.url)