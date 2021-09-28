import requests



ENDPOINT = "http://127.0.0.1:5000/predict"

test_ok = requests.post(ENDPOINT, json={"texte": "j'ai peur du virus"})
print(test_ok, test_ok.json())
