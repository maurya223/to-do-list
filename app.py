from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample in-memory "database"
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"}
]

# GET - Fetch all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200

# GET - Fetch a single user by ID
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

# POST - Create a new user
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the User API! Try /users"}), 200

# PUT - Update a user
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404
    data = request.get_json()
    user["name"] = data.get("name", user["name"])
    user["email"] = data.get("email", user["email"])
    return jsonify(user), 200

# DELETE - Remove a user
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    global users
    users = [u for u in users if u["id"] != user_id]
    return jsonify({"message": "User deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True)
