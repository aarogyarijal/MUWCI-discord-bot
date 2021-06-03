import requests
import json

Joke_URL = "https://sv443.net/jokeapi/v2/joke/Miscellaneous,Dark,Spooky?blacklistFlags=racist,sexist&type=single"
Pun_URL = "https://sv443.net/jokeapi/v2/joke/Miscellaneous,Dark,Spooky?blacklistFlags=racist,sexist&type=twopart"
Comp_URL = "https://complimentr.com/api"
Roast_URL = "https://evilinsult.com/generate_insult.php?lang=en&type=json"
Dad_URL = "https://icanhazdadjoke.com"
Cat_URL = "https://api.thecatapi.com/v1/images/search?size=full"


headers = {'Accept': "application/json"}
headers2 = {'x-api-key': "3adaf0eb-9e7b-45cf-86a7-58bffc34e38a"}
def Dog_URL(breed):
    if breed=="":
        return (f"https://dog.ceo/api/breeds/image/random")
    else:
        return (f"https://dog.ceo/api/breed/{breed}/images/random")
    
def check_valid_status_code(request):
    if request.status_code == 200:
        return request.json()
    return False

def get_cat():
    request = requests.get(Cat_URL, headers=headers2)
    data = check_valid_status_code(request)
    return data

def get_joke():
    request = requests.get(Joke_URL)
    data = check_valid_status_code(request)
    return data

def get_pun():
    request = requests.get(Pun_URL)
    data = check_valid_status_code(request)
    return data

def get_comp():
    request = requests.get(Comp_URL)
    data = check_valid_status_code(request)
    return data

def get_roast():
    request = requests.get(Roast_URL)
    data = check_valid_status_code(request)
    return data

def get_dog(breed):
    URL = Dog_URL(breed)
    request = requests.get(URL)
    print(request, URL)
    data = check_valid_status_code(request)   
    return data

def get_dad():
    request = requests.get(Dad_URL, headers=headers)
    data = check_valid_status_code(request)
    return data