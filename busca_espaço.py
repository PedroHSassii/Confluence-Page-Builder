import requests
from requests.auth import HTTPBasicAuth

BASE_URL = "SUA URL AQUI"
EMAIL = "SEU EMAIL AQUI"
TOKEN = "SEU TOKEN AQUI"

response = requests.get(
    f"{BASE_URL}/wiki/rest/api/space/AA",
    auth=HTTPBasicAuth(EMAIL, TOKEN),
    headers={"Accept": "application/json"}
)

print(response.status_code)
print(response.json())