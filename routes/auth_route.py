from flask import Blueprint, request, jsonify, session, flash
from models.user_model import User, bcrypt

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    if User.find_by_email(data["email"]):
        return jsonify({"message": "Email already registered!"}), 400
    User.register_user(data["email"], data["password"])
    return jsonify({"message": "Registration Successful!"}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.find_by_email(data["email"])
    if user and bcrypt.check_password_hash(user["password"], data["password"]):
        session["email"] = user["email"]
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"message": "Invalid email or password"}), 401

@auth_bp.route("/forgot-password", methods=["POST"])
def forgot_password():
    data = request.json
    user = User.find_by_email(data["email"])
    if user:
        # Send reset email logic here
        return jsonify({"message": "Password reset email sent"}), 200
    return jsonify({"message": "Email not found"}), 404

@auth_bp.route("/logout")
def logout():
    session.clear()
    return jsonify({"message": "Logged out successfully"}), 200