import requests

sheety_endpoint = "https://api.sheety.co/aba2ece9aa1a17eb62a8b40e0be55b8b/flightDeals/prices/"


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data (self):
        sheety_response = requests.get(url=sheety_endpoint)
        data = sheety_response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{sheety_endpoint}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def get_customer_emails(self):
        customers_endpoint = "https://api.sheety.co/aba2ece9aa1a17eb62a8b40e0be55b8b/flightDeals/users"
        response = requests.get(customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data