import requests
import os

SHEETY_URL = os.getenv("SHEETY_URL")
USERS_URL= os.getenv("USERS_URL")
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}
        self.customer_data = {}

    def get_destinationdata(self):

        response = requests.get(url=SHEETY_URL)
        data = response.json()
        self.destination_data= data['prices']
        return(self.destination_data)

    def update_code(self):
        for i in self.destination_data:
            new_data = {
                "price":{
                    "iataCode": i["iataCode"]
                }

            }
            put = requests.put(url=f"{SHEETY_URL}/{i["id"]}",json=new_data)
            # print(put.json())

    def get_customer_emails(self):
        response = requests.get(url=USERS_URL)
        data = response.json()
        # See how Sheet data is formatted so that you use the correct column name!
        # pprint(data)
        # Name of spreadsheet 'tab' with the customer emails should be "users".
        self.customer_data = data["users"]
        return self.customer_data