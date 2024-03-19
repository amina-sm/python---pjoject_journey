import requests
from datetime import datetime
import time

APP_ID = "41e139ee"
API_KEY = "0b2b21cdbd12112d80ec7cbd8f6b298b"

GENDER = "female"
WEIGHT_KG = 50
HEIGHT_CM = 160
AGE = 23

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://docs.google.com/spreadsheets/d/1zmLeTJGl2zza6ob9uo_hYoTxcdqJmTSuTf9-qCjM04Q/edit?usp=sharing"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

retry_count = 3
retry_delay = 5  # seconds

for _ in range(retry_count):
    try:
        response = requests.post(
            exercise_endpoint, json=parameters, headers=headers)
        response.raise_for_status()  # Raise exception for 4xx or 5xx status codes
        result = response.json()
        break  # Break out of the loop if successful
    except (requests.exceptions.RequestException, ValueError) as e:
        print(f"Error occurred: {e}")
        print(f"Retrying in {retry_delay} seconds...")
        time.sleep(retry_delay)
else:
    print("Failed to connect to the Nutritionix API after multiple retries. Please check your connection and try again later.")
    exit()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    try:
        sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
        sheet_response.raise_for_status()  # Raise exception for 4xx or 5xx status codes
        print(sheet_response.text)
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while writing to Google Sheets: {e}")
