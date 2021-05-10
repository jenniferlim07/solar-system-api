import pytest
from app import create_app
from app import db
from app.models.planet import Planet

@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def two_saved_planets(app):
    # Arrange
    water_planet = Planet(name = "Earth",
                    description= "Homebase",
                    diameter = 7917)
    gas_planet = Planet(name = "Jupiter",
                    description="Chonkey-boi",
                    diameter = 86881)

    db.session.add_all([water_planet, gas_planet])
    db.session.commit()

@pytest.fixture
def planet_data(app):
    return {
        "name": "Earth",
        "description": "Homebase",
        "diameter" : 7917
    }
