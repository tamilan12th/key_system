import requests
from flask import Flask

app = Flask(__name__)

response = requests.get('https://bestcash2020.com/oiii')
print(response.url)
print(response.status_code)


@app.route('/')
def hii():
    if not response.url == 'https://ta.ta2deem7arbya.com/2021/11/13/cfd-industry-and-benefits-of-trading-exness/':
        return "Success"
    else:
        return "error"

