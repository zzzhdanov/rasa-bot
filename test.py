import requests as rq

id = 162334994
api = "https://api.opendota.com/api"


# t = rq.get(f"{api}/players/{id}/peers").json()

# sor = sorted(t, key = lambda x: x["games"], reverse=True)

# for i in sor:
# 	print(i)


result = f"Nickname --- {5} \n" \
		 f"Rating --- {8} \n" \
		 f"Win Rate --- {9} \n" \
		 f"DotaPlus Subscription --- {10} \n"

result2 =f"Nickname --- {5} \n" \
		 f"Rating --- {8} \n" \
		 f"Win Rate --- {9} \n" \
		 f"DotaPlus Subscription --- {10} \n"
l = [result, result2]


def te():
	return f"Nickname --- {5} \n" \
		 f"Rating --- {8} \n" \
		 f"Win Rate --- {9} \n" \
		 f"DotaPlus Subscription --- {10} \n"
pt = [te() for _ in range(10)]

# print(str("------------------- \n".join(pt)))

print(int("5"))

l = [1,2,3,4]

print(l[:1000])
