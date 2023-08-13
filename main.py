import time
from nasa_api_key import get_nasa_api_key

import requests
import subprocess
import os
# import pprint
# import json

def get_nasa_image():
    api_key = get_nasa_api_key()
    params = {"api_key": api_key}

    r = requests.get("https://api.nasa.gov/planetary/apod", params=params)
    r_json = r.json()
    # print(pprint.pprint(r_json))
    image_url = r_json['url']
    return image_url

def download_image(image_url, file_path):
    downloaded_image = requests.get(image_url)
    file_path = file_path
    try:
        for _ in range(2):
            with open(file_path, 'wb') as image_file:
                image_file.write(downloaded_image.content) # .content is to extract the binary content
    except Exception as error:
        print(error)

def apple_script(image_path):
    command = f"osascript -e 'tell application \"System Events\" to tell every desktop to set picture to \"{image_path}\"'"
    try:
        subprocess.run(command, shell=True, check=True)
    except Exception as error:
        print(error)
    print("Reached")

def change_wallpaper():
    # os.path.join(os.path.expanduser("~") gets the user path
    image_path1 = os.path.join(os.path.expanduser("~"), "Desktop", "nasa_api", "nasa_wallpapers", "nasa_image_of_the_day1.jpeg")
    image_path2 = os.path.join(os.path.expanduser("~"), "Desktop", "nasa_api", "nasa_wallpapers", "nasa_image_of_the_day2.jpeg")

    # Grabs image of the day url
    image_url = get_nasa_image()
    # image_url = "https://www.allrecipes.com/thmb/0xH8n2D4cC97t7mcC7eT2SDZ0aE=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/6776_Pizza-Dough_ddmfs_2x1_1725-fdaa76496da045b3bdaadcec6d4c5398.jpg"
    # Downloads it
    time.sleep(2)
    download_image(image_url, image_path1)
    download_image(image_url, image_path2)
    print("Complete")
    # Saves it as wallpaper
    # time.sleep(2)
    # apple_script(image_path)

change_wallpaper()


# /Users/kabirguron/Documents/nasa_api
# print(pprint.pprint(r_json))
