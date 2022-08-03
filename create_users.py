import requests

sheety_users = "https://api.sheety.co/aba2ece9aa1a17eb62a8b40e0be55b8b/flightDeals/users"

class CreateUsers:
    print("Welcome to Matthew's Fight Club.\n We Find the best flight deals and email you.")
    fname = input("What is your first name?\n")
    lname = input(f"Okay {fname}, What is your last name?\n")
    email = input(f"{fname} {lname}, what is your email?\n")
    email_conf = input("Type your email again.\n")
    if email == email_conf:
        print("You're in the club! Check your email!")
        user = {
            "user": {
                "firstName": fname,
                "lastName": lname,
                "email": email
            }
        }
        response = requests.post(url=sheety_users, json=user)
    else:
        print("The emails you typed were not the same. Please try again.")
