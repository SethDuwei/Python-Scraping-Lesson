import requests

payload = (('username', 'duwei'), ('password', 'password'))
r = requests.post(
    'http://pythonscraping.com/pages/cookies/welcome.php', data=payload)
print(r.text)
