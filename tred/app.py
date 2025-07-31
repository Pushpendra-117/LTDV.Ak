from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "🎉 App is working fine on Render!"

if __name__ == '__main__':
    app.run()
