from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# In-memory user store
users = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/reset")
def reset():
    return render_template("reset.html")

@app.route("/users")
def user_list():
    return render_template("users.html")

@app.route("/api/create-user", methods=["POST"])
def create_user():
    data = request.get_json()
    users.append({
        "name": data["name"],
        "email": data["email"],
        "role": data["role"]
    })
    return jsonify({"message": f"User {data['name']} created successfully!"})

@app.route("/api/reset-password", methods=["POST"])
def reset_password():
    data = request.get_json()
    return jsonify({"message": f"Password reset for {data['email']}!"})

@app.route("/api/users", methods=["GET"])
def get_users():
    return jsonify({"users": users})