#! python3 

import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(res.status_code)