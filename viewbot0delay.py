import requests

website = open("site.txt", "r").read().strip()
counter = 0
while True:
    response = requests.get(f"{website}")
    counter += 1
    print(f"Request #{counter} - Status Code: {response.status_code}")
