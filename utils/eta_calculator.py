import requests
from datetime import datetime, timedelta
import os

def get_eta(user_location, meetup_location, transport_mode):
    response = requests.get("https://maps.googleapis.com/maps/api/distancematrix/json", {
        'origins': user_location,
        'destinations': meetup_location,
        'mode': transport_mode,
        'key': os.getenv('GOOGLE_MAPS_API_KEY')
    })
    eta = response.json()['rows'][0]['elements'][0]['duration']['value']  # in seconds
    return datetime.now() + timedelta(seconds=eta)
