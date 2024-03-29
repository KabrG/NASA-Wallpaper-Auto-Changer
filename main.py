import time
import datetime
from datetime import date
import tkinter as tk
from nasa_api_key import get_nasa_api_key
import sys
import os

import requests
import subprocess

# Export the DISPLAY environment variable
os.environ['DISPLAY'] = ':0.0'

# IMPORTANT NOTE. Allow cron jobs to have full disk access: https://www.bejarano.io/fixing-cron-jobs-in-mojave/
# Add the directory containing the 'requests' module to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


# import pprint # Displaying Purposes

def get_nasa_image():
    api_key = get_nasa_api_key()
    params = {"api_key": api_key}
    try:
        r = requests.get("https://api.nasa.gov/planetary/apod", params=params)
        r_json = r.json()
        # print(pprint.pprint(r_json)) # Uncomment code for visibility of JSON
        image_url = r_json['url']
        return image_url
    except Exception as error:
        print("Failed to get image: ", error)

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
    print("Wallpaper added (Apple Script)")

def change_wallpaper():
    # os.path.join(os.path.expanduser("~") gets the user path
    date_time = str(datetime.datetime.now())
    # wallpaper_directory = os.path.join(os.path.expanduser("~"), "Documents", "NASA-Wallpaper-Auto-Changer",
    #                            "nasa_api_wallpapers")
    directory_path = os.path.join(os.path.expanduser("~"), "Documents",
                                  "NASA-Wallpaper-Auto-Changer", "nasa_api_wallpapers1")
    image_path1 = os.path.join(directory_path, f"nasa_image_of_the_day_{date_time}_1.jpeg")
    image_path2 = os.path.join(directory_path, f"nasa_image_of_the_day_{date_time}_2.jpeg")

    # Grabs image of the day url
    image_url = get_nasa_image()

    print("Url grabbed")
    # Sample Pizza URL (Testing Purposes)
    # image_url = "https://www.allrecipes.com/thmb/0xH8n2D4cC97t7mcC7eT2SDZ0aE=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/6776_Pizza-Dough_ddmfs_2x1_1725-fdaa76496da045b3bdaadcec6d4c5398.jpg"
    # Downloads it
    time.sleep(2)
    try:
        delete_files_in_directory(directory_path)
    except Exception as error:
        print("A error has occurred: ", error)
    download_image(image_url, image_path1)
    download_image(image_url, image_path2)
    print("Wallpaper Added")
    # ALTERNATIVE METHOD: APPLE SCRIPT
    # Saves it as wallpaper
    # apple_script(image_path)

def delete_files_in_directory(directory_path):
   try:
     files = os.listdir(directory_path) # Gets all files in listed directory
     for file in files:
       file_path = os.path.join(directory_path, file) # Gets an individual file
       if os.path.isfile(file_path): # Checks if it's a file
         os.remove(file_path) # Removes file
     print("All files deleted successfully.")
   except OSError:
     print("Error occurred while deleting files.")


def get_message():
    api_key = get_nasa_api_key()
    params = {"api_key": api_key}
    print("Retrieving explanation")
    r = requests.get("https://api.nasa.gov/planetary/apod", params=params)
    r_json = r.json()
    # print(pprint.pprint(r_json)) # Uncomment code for visibility of JSON
    explanation = r_json['explanation']
    print("Got explanation")
    return explanation

def display_message():
    message = get_message()
    print(message)
    destroy_after_seconds = (24*60*60-30)
    win_height = 550
    win_width = 325
    win = tk.Tk()

    win.title("NASA Explanation: " + str(date.today()))  # title of the GUI window
    win.maxsize(win_width, win_height)  # maxsize of window (length, height)
    win.minsize(win_width, win_height)  # minsize of window (length, height)
    win.config(bg="black")  # specify background color
    win.geometry(f"{win_width}x{win_height}+0+225")  # Where window will open: geometry(width x height + position_right + position_down)

    # Title label
    title_label = tk.Label(win, text="Message of the Day",
                           font=("Courier", 16), fg="white", bg="black")
    title_label.pack()

    # Message label
    fact_widget = tk.Label(win, text=message,
                           font=("Courier", 14, "italic"), fg="white", bg="black", wraplength=win_width-41,
                           anchor="w", justify="left")

    fact_widget.pack(padx=20, pady=10, anchor="w")
    # Destroys window before next session
    win.after(1000*destroy_after_seconds, lambda: win.destroy())
    win.mainloop()

change_wallpaper()
display_message()
