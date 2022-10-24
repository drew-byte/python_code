import requests
import json

def login(mail,password):
    s = requests.Session()
    payload = { 
               'email' : mail,
               'password' : password
               }
    #https://website = URL of any website you want
    res = s.post('https://website', json = payload)
    s.headers.update({'authorization' : json.loads(res.content)['token']})
    
    print(res.content)
    return s 

# email = your mail
# password = your password

session = login('email','password')

#if the website does not have authorization requests this code is none sense xD

r = session.patch('https://website/user/profile', json={'location' : 'Philippines'})
print(r.content)
