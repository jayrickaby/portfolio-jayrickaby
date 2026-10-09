from flask import Flask, render_template
from api import github

app = Flask(__name__)
gh = github.Github()

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/github')
def github():
    return render_template('git-summary.html', repo_count=gh.get_repos())

if __name__ == '__main__':
    app.run(debug=True)