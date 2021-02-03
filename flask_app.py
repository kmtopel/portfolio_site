from flask import Flask, render_template
import requests
import json

github_data = json.loads(requests.get("https://api.github.com/users/kmtopel/repos").text)

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/projects')
def projects():
    return render_template('projects.html', data=github_data)
