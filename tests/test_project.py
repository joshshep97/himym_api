'''
Character route tests
.../api/characters/
'''
def test_get_characters(client):
    response = client.get('/api/characters/')
    assert response.status_code == 200

def test_get_character(client):
    response = client.get('api/characters/1')
    assert response.status_code == 200

'''
Episode route tests
.../api/episodes/
'''
def test_get_episodes(client):
    response = client.get('/api/episodes/')
    assert response.status_code == 200

def test_get_episode(client):
    response = client.get('api/episodes/1')
    assert response.status_code == 200