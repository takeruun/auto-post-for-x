import json
from twitter.account import Account

def pretty_print_json(data):
  print(json.dumps(data, indent=2, sort_keys=True,ensure_ascii=False))

account = Account(cookies='cookies.json')

res = account.tweet('hello')

pretty_print_json(res)