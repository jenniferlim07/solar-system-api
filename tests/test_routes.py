
def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planet")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet(client, two_saved_planets):
    # Act
    response = client.get("/planet/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Earth",
        "description": "Homebase",
        "diameter": 7917
    }

def test_get_one_non_existing_planet(client):
    #Act
    response = client.get("/planet/1")

    #Assert
    assert response.status_code == 404

def test_get_all_planets(client, two_saved_planets):
    # Act
    response = client.get("/planet")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == [{
        "id": 1,
        "name": "Earth",
        "description": "Homebase",
        "diameter": 7917
        },
       { "id": 2,
        "name": "Jupiter",
        "description": "Chonkey-boi",
        "diameter": 86881
       }
    ]

def test_create_one_planet(client, planet_data):
   response = client.post("/planet",
    json=planet_data)
   response_body = response.get_json()

   assert response.status_code == 201
   assert response_body == {"success": True,
        "message": f"Planet Earth has been created"}
