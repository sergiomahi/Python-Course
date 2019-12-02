from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os

import sys

def StartSearch():
    count = 0
    search = input("Search for: ")
    MAX_IMAGES = int(input("How many images do you want? "))

    params = {"q": search}
    DIR_NAME = search.replace(" ", "_").lower()

    if not os.path.isdir(DIR_NAME):
        os.makedirs(DIR_NAME)

    r = requests.get("https://www.bing.com/images/search", params=params)
    soup = BeautifulSoup(r.text, "html.parser")

    links = soup.findAll("a", {"class": "thumb"})

    for item in links:
        try:
            img_obj = requests.get(item.attrs["href"])
            print("Getting {}".format(item.attrs["href"]))
            title = item.attrs["href"].split("/")[-1] # Anything after the final / would be the name
            try:
                img = Image.open(BytesIO(img_obj.content))  # It sometimes dies.
                img.save("./{}/{}".format(DIR_NAME, title), img.format)
            except:
                print("Could not save that image.")
        except:
            print("Could not request that image.")

        count += 1
        if (count == MAX_IMAGES):
            print("Saliendo")
            break
    
    StartSearch()

StartSearch()