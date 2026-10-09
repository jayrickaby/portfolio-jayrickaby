import calendar
import requests

from portfolio.api.apitemplate import ApiTemplate


class Github (ApiTemplate):
    def __init__(self):
        super().__init__()
        self._API_URL: str = f"https://api.github.com"
        self._USER_NAME: str = "jayrickaby"

        self._commit_count: int = 0
        self._merge_count: int = 0
        self._user_data: dict = {}

    def get_bio(self) -> str:
        if self._should_refresh_cache():
            self._refresh_cache()

        if "bio" in self._user_data:
            return self._user_data["bio"]

        return ""

    def get_commit_count(self) -> int:
        if self._should_refresh_cache():
            self._refresh_cache()

        return self._commit_count

    def get_merge_count(self) -> int:
        if self._should_refresh_cache():
            self._refresh_cache()

        return self._merge_count

    def get_repo_count(self) -> int:
        if self._should_refresh_cache():
            self._refresh_cache()

        if "public_repos" in self._user_data:
            return self._user_data["public_repos"]

        return 0

    def _refresh_commit_count(self):
        params = {
            "q": "author:jayrickaby", "per_page": 1
        }

        data = requests.get(f"{self._API_URL}/search/commits", params=params).json()

        if "total_count" in data:
            self._commit_count = data["total_count"]
        else:
            self._commit_count = 0

    def _refresh_merge_count(self):
        params = {
            "q": "author:jayrickaby is:pr is:merged", "per_page": 1
        }

        data = requests.get(f"{self._API_URL}/search/issues", params=params).json()

        if "total_count" in data:
            self._merge_count = data["total_count"]
        else:
            self._merge_count = 0

    def _refresh_user_data(self) -> None:
        user_url = f"{self._API_URL}/users/{self._USER_NAME}"
        self._user_data = requests.get(user_url).json()

    def _refresh_cache(self) -> None:
        self._refresh_commit_count()
        self._refresh_merge_count()
        self._refresh_user_data()
