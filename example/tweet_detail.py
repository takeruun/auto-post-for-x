import json
from twitter.scraper import Scraper

scraper = Scraper(cookies='cookies.json')

res = scraper.tweets_details([1808855842005135421])

entries = res[0]["data"]["threaded_conversation_with_injections_v2"]["instructions"][0]["entries"]
for i, entity in enumerate(entries):
  print("------")
  if i == 0:
    print("ツイートID:", entity["content"]["itemContent"]["tweet_results"]["result"]["legacy"]["id_str"])
    print("内容:", entity["content"]["itemContent"]["tweet_results"]["result"]["legacy"]["full_text"])
  elif i != len(entries) - 1:
    # リプライ
    # ["items"][0] はリプライの最初のツイート
    print("ツイートID:", entity["content"]["items"][0]["item"]["itemContent"]["tweet_results"]["result"]["legacy"]["id_str"])
    print("内容:", entity["content"]["items"][0]["item"]["itemContent"]["tweet_results"]["result"]["legacy"]["full_text"])
