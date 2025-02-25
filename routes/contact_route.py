from flask import Blueprint, request, jsonify
from models.contact_model import Contact

contact_bp = Blueprint("contacts", __name__)

@contact_bp.route("/add", methods=["POST"])
def add_contact():
    data = request.json
    Contact.add_contact(data)
    return jsonify({"message": "Contact added successfully"}), 201

@contact_bp.route("/search/<registration_number>", methods=["GET"])
def search_contact(registration_number):
    contact = Contact.find_by_registration_number(registration_number)
    if contact:
        return jsonify({"contact": contact}), 200
    return jsonify({"message": "Contact not found"}), 404
