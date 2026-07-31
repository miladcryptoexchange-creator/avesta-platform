def test_create_wallet(client):
    # Register and login
    client.post("/api/auth/register", json={
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpass123"
    })
    
    login = client.post("/api/auth/login", json={
        "username": "testuser",
        "password": "testpass123"
    })
    
    token = login.json()["access_token"]
    
    response = client.get("/api/wallet/", headers={
        "Authorization": f"Bearer {token}"
    })
    
    assert response.status_code == 200
    assert "address" in response.json()
