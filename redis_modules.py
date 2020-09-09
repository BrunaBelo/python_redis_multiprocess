# -- coding: utf-8 --
from time import sleep
import requests

def get_user_github(nickname):
  sleep(2)
  response = requests.get('https://api.github.com/users/{0}'.format(nickname))
  responseJson = response.json()
  url_profile = responseJson['html_url']
  name = responseJson['name']
  return "O link do perfil do usuário {0} é {1}".format(name, url_profile)