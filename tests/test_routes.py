
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
    response_body = response.get_json()

    #Assert
    assert response.status_code == 404