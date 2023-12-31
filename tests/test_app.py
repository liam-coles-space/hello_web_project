# Tests for your routes go here

# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"

# === End Example Code ===

"""
When: I make a POST request to /count_vowels
And: I send "eee" as the body parameter text
Then: I should get a 200 response with 3 in the message
"""
def test_post_count_vowels_eee(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eee'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 3 vowels in "eee"'

"""
When: I make a POST request to /count_vowels
And: I send "eunoia" as the body parameter text
Then: I should get a 200 response with 5 in the message
"""
def test_post_count_vowels_eunoia(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eunoia'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 5 vowels in "eunoia"'

"""
When: I make a POST request to /count_vowels
And: I send "mercurial" as the body parameter text
Then: I should get a 200 response with 4 in the message
"""
def test_post_count_vowels_mercurial(web_client):
    response = web_client.post('/count_vowels', data={'text': 'mercurial'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 4 vowels in "mercurial"'

"""
#Post /sort-names
# Parameters:
#   Names: 'Liam', 'Gary', 'Alan', 'Mary'
#   Expected response (200 OK)

'Alan, Gary, Liam, Mary'
"""

def test_post_sort_names(web_client):
    response = web_client.post('/sort-names', data = {'names':'Liam,Gary,Alan,Mary'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alan,Gary,Liam,Mary'
"""
# Request:
GET /names?add=Eddie

# This route should return a list of pre-defined names, plus the name given.

# Expected response (2OO OK):
Julia, Alice, Karim, Eddie
"""

def test_get_names(web_client):
    response = web_client.get('/names', query_string = {'add':'Eddie'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Julia, Alice, Karim, Eddie'

"""
# Request:
GET /names?add=Eddie,Leo

# Expected response (2OO OK):
Alice, Eddie, Julia, Karim, Leo
"""

def test_get_names_multiple(web_client):
    response = web_client.get('/names', query_string = {'add':'Eddie,Leo'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice, Eddie, Julia, Karim, Leo'
    