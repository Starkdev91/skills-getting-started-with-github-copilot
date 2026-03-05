def test_get_activities_returns_all_seeded_activities(client):
    # Arrange
    endpoint = "/activities"

    # Act
    response = client.get(endpoint)
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert len(payload) == 9
    assert "Soccer Team" in payload
    assert payload["Soccer Team"]["max_participants"] == 22


def test_get_activities_returns_expected_activity_schema(client):
    # Arrange
    endpoint = "/activities"

    # Act
    response = client.get(endpoint)
    payload = response.json()
    soccer_team = payload["Soccer Team"]

    # Assert
    assert response.status_code == 200
    assert set(soccer_team.keys()) == {
        "description",
        "schedule",
        "max_participants",
        "participants",
    }
    assert isinstance(soccer_team["participants"], list)
