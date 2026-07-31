def test_list_nfts(client):
    response = client.get("/api/nft/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
