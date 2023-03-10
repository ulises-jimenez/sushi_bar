import requests as r
from pprint import pprint


def get_nytimes():
    answer = r.get('https://www.nytimes.com')
    top_level_html = answer.content[:1000]
    pprint(top_level_html)


if __name__ == '__main__':
    get_nytimes()
