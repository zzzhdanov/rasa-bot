
entities = [{"id":1, "name": "sfield"},
			{"id": 2, "name": "quant"}]



x1 = list(filter(lambda x: x["id"]==1, entities))[0]["name"]
x2 = list(filter(lambda x: x["id"]==2, entities))[0]["name"]
print(x1, x2)
