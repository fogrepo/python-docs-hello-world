from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "A very big hello, Azure enthusiast!  Learning auto deployment of applications using Azure Deployment Center with Github integration!  Takes about 1.5 minutes from Github edit commit to deployment on web server."
