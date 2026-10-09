from flask import Flask, render_template
from api import github

app = Flask(__name__)
gh = github.Github()

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)