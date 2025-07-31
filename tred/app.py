from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "🎉 App is working fine on Render!"

if __name__ == '__main__':
    app.run()
from flask import Flask

app = Flask(__treding__)

@app.route("/")
def home():
    return "Hello from treding app!"
