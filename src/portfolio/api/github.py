import requests

class Github:
    def __init__(self):
        self._USER_NAME: str = "jayrickaby"
        self._API_URL: str = f"https://api.github.com"

        self._user_data: dict = {}

        self.refresh_data()

    def refresh_data(self) -> None:
        user_url = f"{self._API_URL}/users/{self._USER_NAME}"
        self._user_data = requests.get(user_url).json()

    def get_bio(self) -> str:
        if "bio" in self._user_data:
            return self._user_data["bio"]

        return ""

    def get_commits(self) -> int:
        params = {
            "q": "author:jayrickaby", "per_page": 1
        }

        data = requests.get(f"{self._API_URL}/search/commits", params=params).json()

        if "total_count" in data:
            return data["total_count"]

        return 0

    def get_merges(self) -> int:
        params = {
            "q": "author:jayrickaby is:pr is:merged", "per_page": 1
        }

        data = requests.get(f"{self._API_URL}/search/issues", params=params).json()

        if "total_count" in data:
            return data["total_count"]

        return 0

    def get_repos(self) -> int:
        if "public_repos" in self._user_data:
            return self._user_data["public_repos"]

        return 0