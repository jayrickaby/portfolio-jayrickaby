from flask import Flask, render_template
from api import github

app = Flask(__name__)
gh = github.Github()

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/github')
def github():
    message: str = f"repos: {gh.get_repos()}"
    return render_template('git-summary.html', message=message)

if __name__ == '__main__':
    app.run()