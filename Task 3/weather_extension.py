import requests


def load_ipython_extension(ipython):
    conf = requests.get('http://www.mocky.io/v2/5e53c5da2e000065002daee1').json()
    ipython.push({"weather_conf": conf})
