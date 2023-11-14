import requests as rq

class Player:

	api = "https://api.opendota.com/api"

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

		win_rate = round(secondary_api_info["win"] / (secondary_api_info["win"] + secondary_api_info["lose"]), 2)

		result = f"Nickname --- {primary_api_info['profile']['personaname']} \n" \
				 f"Rating --- {primary_api_info['mmr_estimate']['estimate']} \n" \
				 f"Win Rate --- {win_rate} \n" \
				 f"DotaPlus Subscription --- {primary_api_info['profile']['plus']}"


		return result


	def get_teammates(self, value):

		def peer_info(item):
			return f"Nickname --- {item['personaname']} \n" \
		 		   f"Games --- {item['games']} \n" \
		           f"Win  --- {item['with_win']} \n"

		peers = sorted(rq.get(f"{Player.api}/players/{self.id}/peers").json(), key=lambda x: x["games"], reverse=True)[:value]

		result = "------------------------ \n".join([peer_info(item) for item in peers])

		return result


	def get_matches(self, value):

		def matches_info(item):
			return f"ID --- {item['match_id']} \n" \
		 		   f"Duration --- {item['match_id']} \n" \
		           f"Game mode  --- {item['game_mode']} \n" \
		           f"Hero  --- {item['hero_id']} \n" \
		           f"Party size  --- {item['party_size']} \n" 

		matches = rq.get(f"{Player.api}/players/{self.id}/recentMatches").json()[:value]

		result = "------------------------ \n".join([matches_info(item) for item in matches])

		return result

	def get_heroes(self, value):

		def heroes_info(item):
			return f"ID --- {item['hero_id']} \n" \
		 		   f"Games --- {item['games']} \n" \
		           f"Wins  --- {item['with_win']} \n" 

		heroes = sorted(rq.get(f"{Player.api}/players/{self.id}/heroes").json(), key=lambda x: x["games"], reverse=True)[:value]

		result = "------------------------ \n".join([heroes_info(item) for item in heroes])

		return result







		


