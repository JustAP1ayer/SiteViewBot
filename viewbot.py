import requests
import time

website = open("site.txt", "r").read().strip()
counter = 0
delay = float(open("delay.txt", "r").read())
while True:
    time.sleep(delay)
    response = requests.get(f"{website}")
    counter += 1
    print(f"Request #{counter} - Status Code: {response.status_code}")
