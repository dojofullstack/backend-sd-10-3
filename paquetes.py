import requests


# data = requests.get("https://www.linkedin.com/jobs/search?trk=guest_homepage-basic_guest_nav_menu_jobs&position=1&pageNum=0")



def login():
    API = 'https://dummyjson.com/auth/login'

    data = {
        "username": 'emilys',
        "password": 'emilyspass'
    }

    response = requests.post(API, data=data)
    print(response.json())


def getProduct():
    API = 'https://dummyjson.com/products'
    response = requests.get(API)
    print(response.json())

# login()

# getProduct()

