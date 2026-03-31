import requests
import os

SEARCH_URL = "https://www.petfinder.com/search/dogs-for-adoption/?breed=Miniature%20Schnauzer&distance=300"

USER = os.environ["PUSHOVER_USER"]
TOKEN = os.environ["PUSHOVER_TOKEN"]

def send_push(message):

    requests.post(
        "https://api.pushover.net/1/messages.json",
        data={
            "token": TOKEN,
            "user": USER,
            "message": message
        },
    )

def check_schnauzers():

    r = requests.get(SEARCH_URL)

    if "Miniature Schnauzer" in r.text:

        send_push("🚨 Schnauzer listing found near you! Check Petfinder!")

check_schnauzers()
