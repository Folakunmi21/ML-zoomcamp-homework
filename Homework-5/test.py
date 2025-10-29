
import requests

url = "http://localhost:9696/client_score"

client = {
    "lead_source": "organic_search",
    "number_of_courses_viewed": 4,
    "annual_income": 80304.0
}

response = requests.post(url, json=client).json()

print(response)

if response['convert']:
    print('client will probably get a subscription')
else:
    print('client will probably not get a subscription')