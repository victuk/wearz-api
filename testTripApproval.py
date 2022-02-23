import requests

baseurl = "http://localhost:4000/v1/"

true = 'true'

staff1 = {"status":true,"token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjYxNzhjYjg5MmIyMDNhOGJhMDY4YWE3MSIsInJvbGUiOiJzdGFmZiIsImNvbXBhbnlEZXRhaWxzIjoiNjE3OGNiODkyYjIwM2E4YmEwNjhhYTZmIiwibWFuYWdlckRldGFpbHMiOiI2MTc4Y2I4OTJiMjAzYThiYTA2OGFhNzAiLCJpYXQiOjE2MzUzMDYzNzl9.PpEHlfCpTjqt-DoUEd_UiezdivUJen6cU0t0uXdRgGc","email":"staff1@staff1.com"}

driverID = "6178cb892b203a8ba068aa73"

staffID = "6178cb892b203a8ba068aa71"

companyID = "6178cb892b203a8ba068aa6f"

tripID = ["617d1f6039f2ba1c25d7cbaa", "617d1f6039f2ba1c25d7cba9"]


tripArray = []

def modifyTrip():
    for i in range(len(tripID)):
        updatedTripStatus = requests.put(baseurl + "change-trip-status", data = {
        "token": staff1["token"],
        "tripID": tripID[i],
        "status": "approved",
        "driversDetails": driverID
        })
        tripArray.append(updatedTripStatus.json()["changedTrip"]["_id"])
    print("Details sucessfully changed")
    updateManifest()

def updateManifest():
    manifestRes = requests.post(baseurl + "manifest", data = {
    "token": staff1["token"],
    "staffDetails": staffID,
    "driverDetails": driverID,
    "companyDetails": companyID,
    "usersList": tripArray
    })
    print("Manifest has been added.")

modifyTrip()
