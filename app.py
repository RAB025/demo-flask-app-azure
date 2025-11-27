from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>🚀 Hello there from Azure Flask App! made a few changes.</h1><p>Your Flask app is successfully deployed on Azure App Service 🎉</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
