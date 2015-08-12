from flask import Flask
from socket import gethostname

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! I'm server: " + gethostname()

if __name__ == "__main__":
    app.run()
