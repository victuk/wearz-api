import requests

baseurl = "http://localhost:4000/v1/"

true = 'true'

users = [
    {"status":true,"token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjYxYTY1NTIxNTlkYmFjYmIxYmNjMWJiZiIsInJvbGUiOiJ1c2VyIiwiaWF0IjoxNjM4MjkwNzIyfQ.CVEE7a8S1nxGA0JH5Sp0VRWD_0luSv5JXpHlrlBct3E","email":"user1@user1.com","role":"user"},
    {"status":true,"token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjYxYTY1NTIxNTlkYmFjYmIxYmNjMWJjMCIsInJvbGUiOiJ1c2VyIiwiaWF0IjoxNjM4MjkwNzIyfQ.dFQh33tTxI0e39Fotzu4_4f0t_p6xzaMAtfTVaUiKCs","email":"user2@user2.com","role":"user"}
]

company = [
    {"companyID": "61a6552059dbacbb1bcc1bb9"},
    {"companyID": "61a6552059dbacbb1bcc1bb3"}
]

tripsData = [
    {
    "location": "Akwa Ibom",
    "destination": "Lagos",
    "departureDate": "22 Nov 2021"
    },
    {
    "location": "Cross River",
    "destination": "Abuja",
    "departureDate": "25 Nov 2021"
    },
    {
    "location": "Lagos",
    "destination": "Akwa Ibom",
    "departureDate": "26 Nov 2021"
    },
    {
    "location": "Abuja",
    "destination": "Cross River",
    "departureDate": "28 Nov 2021"
    }
]

def generateTripSchema():
    for i in range(len(users)):
        # print(users[i]["token"])
        for j in range(len(tripsData)):
            newTrip = requests.post(baseurl + "request-trip", data = {
            "token": users[i]["token"],
            "location": tripsData[j]["location"],
            "destination": tripsData[j]["destination"],
            "departureDate": tripsData[j]["departureDate"],
            "companyID": company[i]["companyID"]
            })
            print("User with email: " + users[i]["email"] + ", Location: " + tripsData[j]["location"] + " and destination " + tripsData[j]["destination"] + " created")

        print("Request of trip for user " + users[i]["email"] + " complete.")

    print("Creation of sample request trips complete.")

generateTripSchema()
