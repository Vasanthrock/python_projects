import os

import requests
from pprint import pprint


FLIGHT_URL= os.getenv("FLIGHT_URL")
IATA_URL = os.getenv("IATA_URL")
TOKEN_URL = os.getenv("TOKEN_URL")
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.new_token = self.get_token()

    def get_token(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': API_KEY,
            'client_secret': API_SECRET
        }
        response = requests.post(url=TOKEN_URL, headers=header, data=body)
        data = response.json()
        print(f"Your token is {data['access_token']}")
        print(f"Your token expires in {data['expires_in']} seconds")
        return (data['access_token'])

    def get_destination_code(self,city_name):
        headers = {"Authorization": f"Bearer {self.new_token}"}
        query = {
            "keyword": city_name,
            "max": "2",
            "include": "AIRPORTS",
        }
        response = requests.get(
            url=IATA_URL,
            headers=headers,
            params=query
        )
        print(f"Status code {response.status_code}. Airport IATA: {response.text}")
        try:
            code = response.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not Found"
        else:
            return code

    def check_flight(self, origin_city_code, destination_city_code, from_time, to_time, is_direct=True):
        headers = {"Authorization": f"Bearer {self.new_token}"}
        query = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true" if is_direct else "false",
            "currencyCode": "INR",
            "max": "10",
        }
        flight_response = requests.get(url=FLIGHT_URL,headers=headers,params=query)
        if flight_response.status_code != 200:
            print(f"check_flights() response code: {flight_response.status_code}")
            print("There was a problem with the flight search.\n"
                  "For details on status codes, check the API documentation:\n"
                  "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api"
                  "-reference")
            print("Response body:", flight_response.text)
            return None
        return(flight_response.json())