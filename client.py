import requests

class CodingEnvClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def reset(self):
        return requests.post(f"{self.base_url}/reset").json()

    def step(self, code):
        return requests.post(
            f"{self.base_url}/step",
            json={"code": code}
        ).json()