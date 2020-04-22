from flask import Flask, request
app = Flask("UserApp")

@app.route("/users", methods=["POST"])
def add_user():
    user = request.args
    return "success"

if __name__ == "__main__":
    app.run(debug=True)