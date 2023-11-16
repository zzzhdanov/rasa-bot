import requests as rq

class Player:

	api = "https://api.opendota.com/api"

	heroes_map = rq.get(f"{api}/heroes").json()

	def __init__(self, id):
		self.id = id
		self.info = rq.get(f"{Player.api}/players/{self.id}").json()

		if "profile" not in self.info.keys():
			raise ValueError("Profile doesn't exist")

	def get_nickname(self):
		return self.info["profile"]["personaname"]

	def get_brief_info(self):
		primary_api_info = self.info
		secondary_api_info = rq.get(f"{Player.api}/players/{self.id}/wl").json()

		win_rate = round(secondary_api_info["win"] / (secondary_api_info["win"] + secondary_api_info["lose"]) * 100, 2)

		result = f"ID ---------------------- {primary_api_info['profile']['account_id']} \n" \
		         f"Nickname ---------------- {primary_api_info['profile']['personaname']} \n" \
				 f"Rating ------------------ {primary_api_info['mmr_estimate']['estimate']} \n" \
				 f"WRate ------------------- {win_rate}% \n" \
				 f"DotaPlus Subscription --- {primary_api_info['profile']['plus']}"


		return result


	def get_teammates(self, value, sort_field):

		def peer_info(item):
			win_rate = round(item["win"] / item["games"] * 100, 2)

			return f"ID --------- {item['account_id']} \n" \
			       f"Nickname --- {item['personaname']} \n" \
		 		   f"Games ------ {item['games']} \n" \
		           f"WRate ------ {win_rate}% \n"

		field_map = {"wrate": lambda x: (x["win"]/ x["games"]) if x["games"] != 0 else 0,
					 "games": lambda x: x["games"]}

		sort_key = field_map.get(sort_field)

		peers = sorted(rq.get(f"{Player.api}/players/{self.id}/peers").json(), key=sort_key, reverse=True)[:value]

		result = "------------------------ \n".join([peer_info(item) for item in peers])

		return result


	def get_matches(self, value):

		def matches_info(item):
			psize = 0 if not item['party_size'] else item['party_size']
			hname = list(filter(lambda x: x['id'] == item['hero_id'],Player.heroes_map))[0]['localized_name']

			return f"ID ----------- {item['match_id']} \n" \
		           f"Game mode ---- {item['game_mode']} \n" \
		           f"Hero --------- {hname} \n" \
		           f"Party size --- {psize} \n" 

		matches = rq.get(f"{Player.api}/players/{self.id}/recentMatches").json()[:value]

		result = "------------------------ \n".join([matches_info(item) for item in matches])

		return result

	def get_heroes(self, value, sort_field):

		def heroes_info(item):
			win_rate = round(item["win"] / item["games"] * 100, 2)
			hname = list(filter(lambda x: x['id'] == item['hero_id'],Player.heroes_map))[0]['localized_name']

			return f"Name ---- {hname} \n" \
		 		   f"Games --- {item['games']} \n" \
		           f"WRate --- {win_rate}% \n" 

		field_map = {"wrate": lambda x: (x["win"] / x["games"]) if x["games"] != 0 else 0,
					 "games": lambda x: x["games"]}

		sort_key = field_map.get(sort_field)

		heroes = sorted(rq.get(f"{Player.api}/players/{self.id}/heroes").json(), key=sort_key, reverse=True)[:value]

		result = "------------------------ \n".join([heroes_info(item) for item in heroes])

		return result




# a = Player(162334994)
# print(a.get_heroes(3, "wrate"))



		


