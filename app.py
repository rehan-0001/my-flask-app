from flask import Flask, jsonify, request
app=Flask(__name__)

@app.route("/")
def home():
    return "Hello, Application deployed automatically using GitHub Actions!"

if __name__=="__main__":
    app.run()