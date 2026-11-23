from dotenv import load_dotenv
from flask import Flask, render_template

from .jays_apis import github
from .jays_apis import gitgud
from .jays_apis import hackatime

load_dotenv()

app = Flask(__name__)
gh = github.Github()
gg = gitgud.GitGud()
ht = hackatime.Hackatime()

@app.route('/')
def index():
    return render_template(
        'index.html',
        github_commit_count= gh.get_commit_count(),
        github_merge_count= gh.get_merge_count(),
        github_repo_count = gh.get_repo_count(),
        gitgud_commit_count = gg.get_commit_count(),
        gitgud_merge_count = gg.get_merge_count(),
        gitgud_repo_count = gg.get_repo_count(),
        hackatime_current_projects = ht.get_latest_projects()
    )

if __name__ == '__main__':
    app.run(debug=True)