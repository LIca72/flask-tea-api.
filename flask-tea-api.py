from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/tea", methods = ["GET"])
def tea():
    return jsonify(message = "Welcome to the Tea API!")

@app.route("/order", methods = ["POST"])
def order():
    data = request.get_json()
    tea_type = data.get("type", "black")
    return jsonify(message=f"Your {tea_type} tea is being prepared!")
  
