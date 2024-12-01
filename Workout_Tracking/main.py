import requests
import json
import datetime as dt
import os


WEIGHT = 62
HEIGHT= 167.64
AGE = 22
APP_ID = os.environ.get("APP_ID")
APP_KEY = "b9212197b716f90d3b694ebf6c1d5439"
nutrition_url ="https://trackapi.nutritionix.com"
sheety_url="https://api.sheety.co/380dfd0873aad63daffcbab4d7214be5/myWorkouts/workouts"
TOKEN = "Bearer thisisbearer123token"

headers = {
 "x-app-id" : APP_ID ,
 "x-app-key" : APP_KEY,
}

text = input("Tell me what exercise you did:")
body= {
    "query":text,
    "weight_kg":WEIGHT,
    "height_cm":HEIGHT,
    "age":AGE
  }
exercise_url = f"{nutrition_url}/v2/natural/exercise"
response = requests.post(url=exercise_url,headers=headers, json=body)
data = response.json()

today= dt.datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%X")
header = {
    "Authorization": TOKEN
}
for exercise in data['exercises']:
    sheet_body = {
        "workout":{
            "date":date,
            "time":time,
            "exercise": exercise['name'].title(),
            "duration":exercise['duration_min'],
            "calories":exercise["nf_calories"]

        }
    }
    she_response = requests.post(url=sheety_url,json=sheet_body,headers=header)

    print(she_response.json())

