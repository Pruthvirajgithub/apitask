import datetime

import requests

# Base URL
base_url = "https://httpbin.org"

# Function to send GET request and validate response code
def test_get_request():
    response = requests.get(f"{base_url}/get")
    assert response.status_code == 200
    print("GET request successful. Response code:", response.status_code)

# Function to send POST request with JSON body and validate response contains relevant data
def test_post_request():
    payload = {"key": "value"}
    response = requests.post(f"{base_url}/post", json=payload)
    assert response.status_code == 200
    assert response.json()["json"] == payload
    print("POST request successful. Response contains relevant data.")

# Function to validate request with delayed response
def test_delayed_request():
    delay_time = 5
    print(datetime.datetime.now())
    response = requests.get(f"{base_url}/delay/{delay_time}")
    assert response.status_code == 200
    print(datetime.datetime.now())
    print(f"Delayed request with {delay_time} seconds successful.")

# Function to simulate Unauthorized Access
def test_unauthorized_access():
    response = requests.get(f"{base_url}/status/401")
    assert response.status_code == 401
    print("Unauthorized access simulated successfully.")

# Function to simulate a negative scenario (e.g., sending a request to an invalid endpoint)
def test_negative_scenario():
    response = requests.get(f"{base_url}/invalid_endpoint")
    assert response.status_code == 404
    print("Negative scenario simulated successfully.")

