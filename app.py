from flask import Flask

app = Flask(__name__)

@app.route("/wish")
def pleaseWish():
    return "Hello, Jenkins"

if __name__ == "__main__":
    app.run(host = "0.0.0.0")

# 0.0.0.0 ==> all Traffic
# The default port no is always 5000
