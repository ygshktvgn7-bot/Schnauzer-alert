import requests
import json
import smtplib
from email.mime.text import MIMEText

SEARCH_URL = "https://www.petfinder.com/search/dogs-for-adoption/?breed=Miniature%20Schnauzer&distance=300"

EMAIL = "YOUREMAIL@gmail.com"
PASSWORD = "EMAIL_APP_PASSWORD"

DATA_FILE = "seen.json"

def load_seen():
    try:
        with open(DATA_FILE) as f:
            return json.load(f)
    except:
        return []

def save_seen(seen):
    with open(DATA_FILE,"w") as f:
        json.dump(seen,f)

def get_listings():

    r = requests.get(SEARCH_URL)

    dogs = []

    if "Miniature Schnauzer" in r.text:

        dogs.append({
            "name":"Schnauzer Listing",
            "link":SEARCH_URL
        })

    return dogs

def send_email(dog):

    msg = MIMEText(f"""
New Schnauzer Found

Name: {dog['name']}

Link:
{dog['link']}
""")

    msg["Subject"] = "Schnauzer Alert"
    msg["From"] = EMAIL
    msg["To"] = EMAIL

    server = smtplib.SMTP_SSL("smtp.gmail.com",465)
    server.login(EMAIL,PASSWORD)
    server.send_message(msg)
    server.quit()

def run():

    seen = load_seen()

    listings = get_listings()

    for dog in listings:

        if dog["link"] not in seen:

            send_email(dog)

            seen.append(dog["link"])

    save_seen(seen)

run()
