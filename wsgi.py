from flask import Flask
application = Flask(__name__)

@application.route("/Erwin")
def hello():
    return "Hello World!"

@application.route("/Ron")
def helloR():
    return "Hello Ron!"

@application.route("/Maurits")
def helloM():
    return "Je staat op Mute!"



if __name__ == "__main__":
    application.run()
