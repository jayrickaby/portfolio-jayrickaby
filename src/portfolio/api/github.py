import requests

class Github:
    def __init__(self):
        self._USER_NAME: str = "jayrickaby"
        self._USER_URL: str = f"https://api.github.com/users/{self._USER_NAME}"

        self._user_data: dict = {}

        self.refresh_data()

    def refresh_data(self) -> None:
        self._user_data = requests.get(self._USER_URL).json()

    def get_bio(self) -> str:
        if "bio" in self._user_data:
            return self._user_data["bio"]

        return ""

    def get_repos(self) -> int:
        if "public_repos" in self._user_data:
            return self._user_data["public_repos"]

        return 0