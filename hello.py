from flask import Flask
app = Flask(__name__)
 
@app.route("/")
def hello():
    return "Hello World!"

@app.route("/marco")
def marco():
    return "Polo"
 
if __name__ == "__main__":
    app.run()
