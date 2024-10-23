import requests
from requests.auth import HTTPBasicAuth

# Replace with your Turbonomic server URL and API endpoint
turbonomic_base_url = 'https://your-turbonomic-server/api/v3'
api_endpoint = '/markets'  # Example endpoint, modify as needed

# Replace with your Turbonomic username and password
username = 'your_username'
password = 'your_password'

# Complete API URL
url = f'{turbonomic_base_url}{api_endpoint}'

# Make the GET request using Basic Authentication
response = requests.get(url, auth=HTTPBasicAuth(username, password))

# Check the response status code
if response.status_code == 200:
    # Successfully retrieved the response
    data = response.json()
    print(data)
else:
    # Handle errors
    print(f"Failed to fetch data: {response.status_code}")
    print(response.text)