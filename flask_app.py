from flask import Flask, render_template
import requests
import json

github_data = json.loads(requests.get("https://api.github.com/users/kmtopel/repos").text)

for i in github_data:
    print(i['name'])
    print(i['url'])
    print(i['description'])
    print('\n')


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('main.html',data=github_data)

