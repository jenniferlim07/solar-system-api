from flask import request, Blueprint, make_response
from app import db
from flask import jsonify
from .models.planet import Planet

planet_bp = Blueprint("planet", __name__, url_prefix="/planet")

@planet_bp.route("", methods=["POST"], strict_slashes=False)
def add_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                        description=request_body["description"],
                        diameter=request_body["diameter"])
    
    db.session.add(new_planet)
    db.session.commit()

    return jsonify({
        "success": True,
        "message": f"Planet {new_planet.name} has been created"
    }), 201


@planet_bp.route("", methods=["GET"], strict_slashes=False)
def planet_index():
    planets = Planet.query.all()
    planet_response = []
    for planet in planets:
        planet_response.append(planet.to_json())
    return jsonify(planet_response), 200


@planet_bp.route("/<planet_id>", methods=["GET"], strict_slashes=False)
def get_planet(planet_id):
    planet = Planet.query.get(planet_id)

    if planet:
        return planet.to_json(), 200

    return jsonify({
        "message": f"Planet with id {planet_id} was not found",
        "success" : False
    }), 404

@planet_bp.route("/<planet_id>", methods=["PUT"], strict_slashes=False)
def update_planet(planet_id):
    planet = Planet.query.get(planet_id)
    if planet:
        form_data = request.get_json()
        planet.name = form_data["name"]
        planet.description = form_data["description"]
        planet.diameter = form_data["diameter"]
        db.session.commit()
        return jsonify({
                "success": True,
                "message": f"Planet #{planet.id} successfully updated"
            }), 200
    return jsonify({
        "message": f"Planet with id {planet_id} was not found",
        "success" : False
    }), 404

@planet_bp.route("/<planet_id>", methods=["DELETE"], strict_slashes=False)
def delete_planet(planet_id):
    planet = Planet.query.get(planet_id)
    if planet:
        db.session.delete(planet)
        db.session.commit()
        return jsonify({
            "success": True,
            "message": f"Planet #{planet.id} successfully deleted"
        }), 200
    return jsonify({
        "message": f"Planet with id {planet_id} was not found",
        "success" : False
    }), 404
        



