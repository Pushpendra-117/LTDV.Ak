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

import os
from flask import Flask

app = Flask(__treding__)

@app.route("/")
def home():
    return "Hello from Render!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Render deployment!"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
