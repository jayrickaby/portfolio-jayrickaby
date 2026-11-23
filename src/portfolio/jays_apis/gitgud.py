import calendar
import requests

from portfolio.jays_apis.apitemplate import ApiTemplate


class GitGud (ApiTemplate):
    def __init__(self):
        super().__init__()
        self._API_URL: str = f"https://gitgud.io/api/v4/"
        self._USER_ID: int = 107746

        self._commit_count: int = 0
        self._merge_count: int = 0
        self._repository_count: int = 0

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

        return self._repository_count

    def _refresh_commit_count(self):
        params = {
            "action": "pushed",
            "per_page": 1
        }

        data = requests.get(f"{self._API_URL}/users/{self._USER_ID}/events", params).headers

        if "x-total" in data:
            self._commit_count = int(data["x-total"])
        else:
            self._commit_count = 0

    def _refresh_merge_count(self):
        params = {
            "author_id" : self._USER_ID,
            "per_page": 1,
            "scope": "all"
        }

        data = requests.get(f"{self._API_URL}/merge_requests", params).headers

        if "x-total" in data:
            self._merge_count = int(data["x-total"])
        else:
            self._merge_count = 0

    def _refresh_repository_count(self) -> None:
        params = {
            "per_page": 1
        }

        data = requests.get(f"{self._API_URL}/users/{self._USER_ID}/projects", params).headers

        if "x-total" in data:
            self._repository_count = int(data["x-total"])
        else:
            self._repository_count = 0

    def _refresh_cache(self) -> None:
        self._refresh_commit_count()
        self._refresh_merge_count()
        self._refresh_repository_count()
