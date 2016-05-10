#!/usr/bin/python

from errbot import BotPlugin, botcmd
from subprocess import check_output

import requests

def get_data(url):
  try:
    response = requests.get(url)
    if response.status_code == requests.codes.ok:
      return response.json()
    else:
      raise Exception(response.content)
  except Exception as e:
    raise Exception(e)

class chuck(BotPlugin):

    @botcmd
    def chuck(self, msg, args):
        data = get_data("http://api.icndb.com/jokes/random")
        return data['value']['joke']

