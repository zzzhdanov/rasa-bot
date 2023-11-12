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


