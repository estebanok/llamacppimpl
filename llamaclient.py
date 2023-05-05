import requests
import json

url = "http://localhost:8002/model"

payload = json.dumps({
    "text": "Here goes your prompt text. Answer:"
})
headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, data=payload, headers=headers)

print(response.json())
