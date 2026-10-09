from flask import Flask, render_template
from api import github

app = Flask(__name__)
gh = github.Github()

@app.route('/')
def index():
    return render_template(
        'index.html',
        git_commit_count= gh.get_commits(),
        git_merge_count= gh.get_merges(),
        git_repo_count = gh.get_repos()
    )

if __name__ == '__main__':
    app.run(debug=True)