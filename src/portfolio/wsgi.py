from dotenv import load_dotenv
from flask import Flask, render_template

from api import github

load_dotenv()

app = Flask(__name__)
gh = github.Github()

@app.route('/')
def index():
    return render_template(
        'index.html',
        git_commit_count= gh.get_commit_count(),
        git_merge_count= gh.get_merge_count(),
        git_repo_count = gh.get_repo_count()
    )

if __name__ == '__main__':
    app.run(debug=True)