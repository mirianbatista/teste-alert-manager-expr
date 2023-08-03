import requests
import time
import random

url = "http://0.0.0.0:8000/increase"

while True:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Increase request sent successfully.")
        else:
            print(f"Failed to send increase request. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

    sleep_time = random.randint(1, 15)
    print(f"Sleeping for {sleep_time} seconds...")
    time.sleep(sleep_time)
