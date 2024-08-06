from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'sodha_govt'


if __name__ == "__main__":
    app.run()
