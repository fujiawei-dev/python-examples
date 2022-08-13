from pprint import pprint

import feedparser
import requests

content = requests.get("https://bangumi.moe/rss/latest").text

rss = feedparser.parse(content)

pprint(rss["entries"][0])
