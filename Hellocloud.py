from flask import Flask
server = Flask(__name__)

@server.route("/")
def hello():
    return "Hello from Thinnaphat Server"

if __name__ == "__main__":
    server.run(host='localhost', port=80)