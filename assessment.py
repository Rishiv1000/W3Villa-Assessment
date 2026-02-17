from datetime import datetime
import math

resource = {
    "Name" : "GYM",
    "Capacity":2,
    "Current_Users":{}
}

firsthr_cost= 30
additionalhr_cost= 10

def startuse(username):
    if len(resource["Current_Users"]) >= resource["Capacity"]:
        print("Resouce Capacity is Full, You Are Not Allowed :", username)

    resource["Current_Users"][username] = datetime.now()

def leave_res(username):
    starttimeofuser = resource["Current_Users"][username]
    endtimeofuser= datetime.now()
    totalmin = (endtimeofuser - starttimeofuser).total_seconds() / 60
    totalhr = math.ceil(totalmin/60)
    if(totalhr<=1):
        totalcost= firsthr_cost
    else:
        totalcost= firsthr_cost + (totalhr-1)*additionalhr_cost
    
    print("YOUR BILL : ----")
    print("USER NAME : ", username)
    print("USER START TIME : ", starttimeofuser)
    print("USER END TIME : ", endtimeofuser)
    print("TOTAL USAGE COST : ", totalcost)
    del resource["Current_Users"][username]

while True:
    print("Enter 1 for Start Use")
    print("Enter 2 for End Use")
    print("Enter 3 for See Active Users")
    n = int(input("option choose : "))
    if(n==1):
        name=input("Your Name for Start Use : ")
        startuse(name)
    elif(n==2):
        name=input("Your Name for End Use :")
        leave_res(name)
    else:
        print(resource['Current_Users'])

