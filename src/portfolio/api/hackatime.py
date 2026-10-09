from datetime import datetime
import requests

from portfolio.api.apitemplate import ApiTemplate

class Hackatime (ApiTemplate):
    def __init__(self):
        super().__init__()
        self._API_URL: str = f"https://hackatime.hackclub.com"
        self._USER_NAME: str = "jayrickaby"

        self._latest_projects: list = []

    def get_latest_projects(self):
        if self._should_refresh_cache():
            self._refresh_cache()

        return self._latest_projects

    def _convert_time_to_relative(self, raw_time: str) -> int:
        current_time = self._get_current_time()
        time = current_time

        if raw_time:
            time -= int(datetime.fromisoformat(raw_time).timestamp()) or 0

        return time

    def _refresh_cache(self):
        self._refresh_latest_projects()

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

            time = self._convert_time_to_relative(raw_project["last_heartbeat"])

            hours, remainder = divmod(time, 3600)
            minutes = remainder // 60

            time_str: str = ""

            if hours >= 168:
                pass
            if hours >= 1:
                time_str = f"{hours}h ago"
            elif minutes >= 15:
                time_str = f"{minutes}m ago"
            else:
                time_str = "Now"

            projects.append({
                "name": raw_project["name"] or "",
                "link": raw_project["repo_url"] or "",
                "lastEditTime": time_str
            })

        print(projects)
        self._latest_projects = projects