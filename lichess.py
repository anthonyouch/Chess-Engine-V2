import requests
import json

class LichessAPI:

    def __init__(self):
        self.token = "lip_drFmC9zrFuqtzyNdvs77"
        self.session = requests.Session()

        self.header = {
            "Authorization": f"Bearer {self.token}"
        }

        self.session.headers.update(self.header)

    def get_event(self):
        url = "https://lichess.org/api/stream/event"
        response = self.session.get(url, stream=True)
        for line in response.iter_lines():
            if line:
                print(json.loads(line))
                return json.loads(line)
        return ("ERROR", response)

    def accept_challenge(self, challengeId):
        url = f"https://lichess.org/api/challenge/{challengeId}/accept"
        self.session.post(url)

    def make_move(self, gameId, move):
        """https://lichess.org/api/bot/game/{gameId}/move/{move}"""
        url = f"https://lichess.org/api/bot/game/{gameId}/move/{move}"
        self.session.post(url)

while True:
    lichessAPI = LichessAPI()
    response = lichessAPI.get_event()
    # if response == "challenge":

    # print("response: ", response)
    responseType = response['type']
    if responseType == "challenge":
        challengeID = response["challenge"]["id"]
        lichessAPI.accept_challenge(challengeID)
    elif responseType == "gameStart":
        gameId = response['game']['gameId']
        lichessAPI.make_move(gameId, "e2e4")


    # for line in response.iter_lines():
    #     if line:
    #         print(json.loads(line))
    #         if json.loads(line)['type'] == "challenge":
    #             print(json.loads(line)['challenge']['id'])
    #             lichessAPI.accept_challenge(json.loads(line)['challenge']['id'])
    #
    #         elif json.loads(line)['type'] == "gameStart":
    #             print(json.loads(line)['game']['gameId'])
    #             gameId = json.loads(line)['game']['gameId']
    #             # for now assume we're white and make e2e4 move
    #             lichessAPI.make_move(gameId, "e2e4")