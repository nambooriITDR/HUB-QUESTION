from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to HUB-QUESTION</h1><p>This is my Python-based site.</p>"

@app.route("/about")
def about():
    return "<h1>About</h1><p>Hi,  This site shares my projects and ideas.</p>"

if __name__ == "__main__":
    app.run(debug=True)
