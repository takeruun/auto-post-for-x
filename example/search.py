import json
from twitter.search import Search

def pretty_print_json(data):
    print(json.dumps(data, indent=2, sort_keys=True,ensure_ascii=False))

search = Search(cookies='cookies.json')
res = search.run(
  limit=1,
  retries=1,
  queries=[
      {
          'category': 'Top',
          'query': '副業',
      },
  ],
)

pretty_print_json(res)