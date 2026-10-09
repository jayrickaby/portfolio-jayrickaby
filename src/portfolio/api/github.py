import requests

class Github:
    def __init__(self):
        self._USERNAME: str = "jayrickaby"
        self._USERURL: str = f"https://api.github.com/users/{self._USERNAME}"

    def get_bio(self):
        data: dict = requests.get(self._USERURL).json()

        return data["bio"]

