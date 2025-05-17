from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "自己手搓的网站"
app.run()