import requests as rq
import pprint

pp = pprint.PrettyPrinter()

id = 1174043788


t = rq.get(f"https://api.opendota.com/api/players/{id}")
pp.pprint(t.json())