import requests
from bs4 import BeautifulSoup
import random

# Define the URL of the Yelp collection
url = "https://www.yelp.com/collection/H1HAmJ5WSTj5_ZG4OIa_Aw/Kelly-Kate-Eat-NY"

# Send an HTTP GET request to fetch the web page content
info = requests.get(url)

if info.status_code == 200:
     soup = BeautifulSoup(info.text, 'html.parser')
     restaurant_names = soup.find_all(class_='biz-name')
     random_restaurant = random.choice(restaurant_names).text
     print("You should totally check out this restaurant:", random_restaurant)
else:
    print("Failed to retrieve the web page. Status code:", info.status_code)
