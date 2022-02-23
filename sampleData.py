import requests

baseurl = "http://localhost:4000/v1/"

tokensfile = open("exampleTokens.txt","w+")

usersDict = [
    {
    "firstName": "User",
    "lastName": "One",
    "gender": "male",
    "email": "user1@user1.com",
    "role": "user",
    "location": "Akwa Ibom State",
    "password": "mfreke"
    },
    {
    "firstName": "User",
    "lastName": "Two",
    "gender": "female",
    "email": "user2@user2.com",
    "role": "user",
    "location": "Akwa Ibom State",
    "password": "mfreke"
    }
]

adminDict = [
    {
    "firstName": "Admin",
    "lastName": "One",
    "companyName": "Transport Company One",
    "gender": "male",
    "nextOfKin": "Son",
    "email": "admin1@admin1.com",
    "role": "admin",
    "location": "Akwa Ibom State",
    "password": "mfreke"
    },
    {
    "firstName": "Admin",
    "lastName": "Two",
    "companyName": "Transport Company Two",
    "gender": "female",
    "nextOfKin": "Daughter",
    "email": "admin2@admin2.com",
    "role": "admin",
    "location": "Akwa Ibom State",
    "password": "mfreke"
    }
]

managerDict = [
    {
    "firstName": "Manager",
    "lastName": "One",
    "gender": "female",
    "email": "manager1@manager1.com",
    "role": "manager",
    "location": "Akwa Ibom State",
    "password": "mfreke"
    },
    {
    "firstName": "Manager",
    "lastName": "Two",
    "gender": "female",
    "email": "manager2@manager2.com",
    "role": "manager",
    "location": "Akwa Ibom State",
    "password": "mfreke"
    }
]


staffDict = [
    {
    "firstName": "Staff",
    "lastName": "Two",
    "gender": "male",
    "email": "staff1@staff1.com",
    "phoneNumber": "08137249484",
    "role": "staff",
    "location": "Akwa Ibom State",
    "password": "mfreke"
    },
    {
    "firstName": "Staff",
    "lastName": "Two",
    "gender": "male",
    "email": "staff2@staff2.com",
    "phoneNumber": "08137249484",
    "role": "staff",
    "location": "Akwa Ibom State",
    "password": "mfreke"
    },
    {
    "firstName": "Staff",
    "lastName": "Three",
    "gender": "female",
    "phoneNumber": "08137249484",
    "email": "staff3@staff3.com",
    "role": "staff",
    "location": "Akwa Ibom State",
    "password": "mfreke"
    },
    {
    "firstName": "Staff",
    "lastName": "Three",
    "gender": "female",
    "phoneNumber": "08137249484",
    "email": "staff4@staff4.com",
    "role": "staff",
    "location": "Akwa Ibom State",
    "password": "mfreke"
    }
]

driverDict = [
    {
    "firstName": "Driver",
    "lastName": "One",
    "gender": "male",
    "plateNumber": "la489efw",
    "email": "driver1@driver1.com",
    "role": "driver",
    "location": "Akwa Ibom State",
    "password": "mfreke"
    },
    {
    "firstName": "Driver",
    "lastName": "Two",
    "gender": "male",
    "plateNumber": "la489efx",
    "email": "driver2@driver2.com",
    "role": "driver",
    "location": "Akwa Ibom State",
    "password": "mfreke"
    },
    {
    "firstName": "Driver",
    "lastName": "Three",
    "gender": "male",
    "plateNumber": "la489efb",
    "email": "driver3@driver3.com",
    "role": "driver",
    "location": "Akwa Ibom State",
    "password": "mfreke"
    },
    {
    "firstName": "Driver",
    "lastName": "Four",
    "gender": "male",
    "plateNumber": "la489efk",
    "email": "driver4@driver4.com",
    "role": "driver",
    "location": "Akwa Ibom State",
    "password": "mfreke"
    }
]

def initializeRegisterFunction():
    registerAdmins()
    registerUsers()
    loginManager()
    loginStaff()
    loginDriver()



def registerAdmins():
    for i in range(len(usersDict)):
        admin = requests.post(baseurl + "register", data = {
        "firstName": adminDict[i]["firstName"],
        "lastName": adminDict[i]["lastName"],
        "companyName": adminDict[i]["companyName"],
        "gender": adminDict[i]["gender"],
        "nextOfKin": adminDict[i]["nextOfKin"],
        "email": adminDict[i]["email"],
        "role": adminDict[i]["role"],
        "location": adminDict[i]["location"],
        "password": adminDict[i]["password"]
        })
        if admin.json()["message"] == 'ok':
            print("Admin" + str(i+1) + " created.")
        else:
            print("Couldn't create Admin" + str(i))

        manager = requests.post(baseurl + "registerworkers/reg-manager-admin", data = {
        "firstName": managerDict[i]["firstName"],
        "lastName": managerDict[i]["lastName"],
        "gender": managerDict[i]["gender"],
        "email": managerDict[i]["email"],
        "role": managerDict[i]["role"],
        "location": managerDict[i]["location"],
        "password": managerDict[i]["password"],
        "companyDetails": admin.json()["user"]["_id"]
        })
        if admin.json()["message"] == 'ok':
            print("Manager" + str(i+1) + " created.")
        else:
            print("Couldn't create Manager" + str(i))
        registerStaff(admin, manager, i)
        registerDriver(admin, manager, i)

    for i in range(len(adminDict)):
        admin = requests.post(baseurl + "login", data = {
        "email": adminDict[i]["email"],
        "password": adminDict[i]["password"]
        })
        addAdmin = open("exampleTokens.txt", 'a')
        addAdmin.write(adminDict[i]["email"] + ": " + admin.text + "\n\n")
        addAdmin.close()
        print("Admin" + str(i+1) + " Logged in.")

def registerUsers():
    for i in range(len(usersDict)):
        user = requests.post(baseurl + "register", data = {
        "firstName": usersDict[i]["firstName"],
        "lastName": usersDict[i]["lastName"],
        "gender": usersDict[i]["gender"],
        "email": usersDict[i]["email"],
        "role": usersDict[i]["role"],
        "location": usersDict[i]["location"],
        "password": usersDict[i]["password"]
        })
        print("User" + str(i+1) + " created")
    for i in range(len(usersDict)):
        usertoken = requests.post(baseurl + "login", data = {
        "email": usersDict[i]["email"],
        "password": usersDict[i]["password"],
        })
        addUser = open("exampleTokens.txt", 'a')
        addUser.write(usersDict[i]["email"] + ": " + usertoken.text + "\n\n")
        addUser.close()
        print("User" + str(i+1) + " Logged in.")



def loginManager():
    for i in range(len(managerDict)):
        manager = requests.post(baseurl + "login", data = {
        "email": managerDict[i]["email"],
        "password": managerDict[i]["password"],
        })
        addManager = open("exampleTokens.txt", 'a')
        addManager.write(managerDict[i]["email"] + ": " + manager.text + "\n\n")
        addManager.close()
        print("Manager" + str(i+1) + " Logged in.")



def registerStaff(admin, managerin, i):
    if i == 0:
        for j in range(2):
            manager = requests.post(baseurl + "registerworkers/reg-staff", data = {
            "firstName": staffDict[j]["firstName"],
            "lastName": staffDict[j]["lastName"],
            "gender": staffDict[j]["gender"],
            "email": staffDict[j]["email"],
            "phoneNumber": staffDict[j]["phoneNumber"],
            "role": staffDict[j]["role"],
            "location": staffDict[j]["location"],
            "password": staffDict[j]["password"],
            "companyDetails": admin.json()["user"]["_id"],
            "managerDetails": managerin.json()["user"]["_id"]
            })
            print("Staff" + str(j) + " registered sucessfully")
    elif i == 1:
        for k in range(2):
            manager = requests.post(baseurl + "registerworkers/reg-staff", data = {
            "firstName": staffDict[k+2]["firstName"],
            "lastName": staffDict[k+2]["lastName"],
            "gender": staffDict[k+2]["gender"],
            "email": staffDict[k+2]["email"],
            "phoneNumber": staffDict[k+2]["phoneNumber"],
            "role": staffDict[k+2]["role"],
            "location": staffDict[k+2]["location"],
            "password": staffDict[k+2]["password"],
            "companyDetails": admin.json()["user"]["_id"],
            "managerDetails": managerin.json()["user"]["_id"]
            })
            print("Staff" + str(k+2) + " registered sucessfully")

def registerDriver(admin, managerin, i):
    if i == 0:
        for j in range(2):
            manager = requests.post(baseurl + "registerworkers/reg-driver", data = {
            "firstName": driverDict[j]["firstName"],
            "lastName": driverDict[j]["lastName"],
            "gender": driverDict[j]["gender"],
            "plateNumber": driverDict[j]["plateNumber"],
            "email": driverDict[j]["email"],
            "role": driverDict[j]["role"],
            "location": driverDict[j]["location"],
            "password": driverDict[j]["password"],
            "companyDetails": admin.json()["user"]["_id"],
            "managerDetails": managerin.json()["user"]["_id"]
            })
            print("Driver" + str(j) + " registered sucessfully")
    elif i == 1:
        for k in range(2):
            manager = requests.post(baseurl + "registerworkers/reg-driver", data = {
            "firstName": driverDict[k+2]["firstName"],
            "lastName": driverDict[k+2]["lastName"],
            "gender": driverDict[k+2]["gender"],
            "plateNumber": driverDict[k+2]["plateNumber"],
            "email": driverDict[k+2]["email"],
            "role": driverDict[k+2]["role"],
            "location": driverDict[k+2]["location"],
            "password": driverDict[k+2]["password"],
            "companyDetails": admin.json()["user"]["_id"],
            "managerDetails": managerin.json()["user"]["_id"]
            })
            print("Driver" + str(k+2) + " registered sucessfully")

def loginStaff():
    for i in range(len(staffDict)):
        staff = requests.post(baseurl + "login", data = {
        "email": staffDict[i]["email"],
        "password": staffDict[i]["password"],
        })
        addStaff = open("exampleTokens.txt", 'a')
        addStaff.write(staffDict[i]["email"] + ": " + staff.text + "\n\n")
        addStaff.close()
        print("Staff" + str(i+1) + " Logged in.")


def loginDriver():
    for i in range(len(driverDict)):
        driver = requests.post(baseurl + "login", data = {
        "email": driverDict[i]["email"],
        "password": driverDict[i]["password"],
        })
        addDriver = open("exampleTokens.txt", 'a')
        addDriver.write(driverDict[i]["email"] + ": " + driver.text + "\n\n")
        addDriver.close()
        print("Driver" + str(i+1) + " Logged in.")

initializeRegisterFunction()
