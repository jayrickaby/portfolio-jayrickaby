
from portfolio.api.apitemplate import ApiTemplate

import requests

class Hackatime (ApiTemplate):
    def __init__(self):
        super().__init__()
        self._API_URL: str = f"https://hackatime.hackclub.com"
        self._USER_NAME: str = "jayrickaby"

        self._latest_projects: dict = {}

    def get_latest_projects(self):
        self._refresh_latest_projects()
        return self._latest_projects

    def _refresh_latest_projects(self):
        raw_names: dict = requests.get(f"{self._API_URL}/api/v1/users/{self._USER_NAME}/projects").json() or {}

        if not raw_names:
            return []

        if "projects" not in raw_names or not raw_names["projects"]:
            return []

        names: list[str] = raw_names["projects"]

        projects: list[dict] = []

        for name in names:
            raw_project: dict = requests.get(f"{self._API_URL}/api/v1/users/{self._USER_NAME}/project/{name}").json() or {}

            if not raw_project:
                pass
            if "name" not in raw_project:
                pass
            if "last_heartbeat" not in raw_project:
                pass

            projects.append({
                "name": raw_project["name"] or "",
                "link": raw_project["repo_url"] or "",
                "lastEditTime": raw_project["last_heartbeat"] or ""
            })


        self._latest_projects = projects