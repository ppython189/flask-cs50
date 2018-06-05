from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!!!!"

@app.route("/user")
def index():
    return "Hello user"

if __name__ == '__main__':
    app.run(debug=True)



