from flask import Flask
from api import github

app = Flask(__name__)
gh = github.Github()

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/github')
def github():
    return f"repos: {gh.get_repos()}"

if __name__ == '__main__':
    app.run(debug=True)