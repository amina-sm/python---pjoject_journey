import requests
from datetime import datetime
from math import radians, sin, cos, sqrt, atan2
import time
import smtplib

# Your latitude and longitude
MY_LAT = -6.792354
MY_LONG = 39.208328
MY_EMAIL = "PUT YOUR EMAIL HERE"
MY_PASSWORD = "PUT YOUR PASSWORD HERE"


def is_iss_close(lat1, long1, lat2, long2):
    """
    Function to check if the ISS is close to the given position.
    """
    # Convert degrees to radians
    lat1_rad = radians(lat1)
    long1_rad = radians(long1)
    lat2_rad = radians(lat2)
    long2_rad = radians(long2)

    # Radius of the Earth in km
    earth_radius = 6371.0

    # Haversine formula to calculate distance
    dlon = long2_rad - long1_rad
    dlat = lat2_rad - lat1_rad
    a = sin(dlat / 2)**2 + cos(lat1_rad) * cos(lat2_rad) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = earth_radius * c

    # Check if distance is within 5 degrees (approximately 555 km)
    return distance <= 555


def send_email(message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="PUT RECIEVER EMAIL HERE",  # Fixed: Added quotes around email address
                            msg=f"Subject: Motivation\n\n{message}")
    print("Email sent:", message)


# API URLs
iss_url = "http://api.open-notify.org/iss-now.json"
sun_url = "https://api.sunrise-sunset.org/json"

while True:
    # Get ISS position data
    response = requests.get(iss_url)
    response.raise_for_status()
    iss_data = response.json()

    # Get ISS position
    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])

    # Check if ISS is close
    if is_iss_close(MY_LAT, MY_LONG, iss_latitude, iss_longitude):
        # Get sunrise and sunset data
        sun_params = {
            "lat": MY_LAT,
            "lng": MY_LONG,
            "formatted": 0,
        }
        response = requests.get(sun_url, params=sun_params)
        response.raise_for_status()
        sun_data = response.json()

        # Get current time
        time_now = datetime.now()

        # Get sunset and sunrise times
        sunrise_time = datetime.fromisoformat(sun_data["results"]["sunrise"])
        sunset_time = datetime.fromisoformat(sun_data["results"]["sunset"])

        # Check if it's currently dark
        if time_now < sunrise_time or time_now > sunset_time:
            # Send email notification
            send_email("Look up! ISS is close and it's currently dark.")

    # Wait for 60 seconds before checking again
    time.sleep(60)
