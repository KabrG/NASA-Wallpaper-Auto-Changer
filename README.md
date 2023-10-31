# NASA-Wallpaper-Auto-Changer
 
## Description
NASA posts a daily astronomy photo of the day. The goal for this project was to automate changing my desktop wallpaper background daily while posting the explanation on a Tkinter window for display. I used python to change the wallpaper itself and CronJob to schedule the execution daily. For this project, my MacOS wallpaper refreshes at 00:10 

<img width="1439" alt="Screen Shot 2023-08-16 at 21 37 54" src="https://github.com/KabrG/NASA-Wallpaper-Auto-Changer/assets/130770806/4a876d8b-5e59-49d1-a50a-a9d27edfb009">

## Installation 
The project runs on Python3. Ensure that the module Tkinter is imported correctly with any virtual enviroments set appropiately. 
## Operation
Essentially, MacOS allows users to create a folder that the system can cycle through periodically to change the wallpaper. Therefore, changing the contents of the folder will change which wallpapers will be displayed.
The project can be divided into the following procedures: 
1. Retrieve the image URL and explanation of the day message using the NASA API
2. Delete all preexisting wallpapers in the folder 
3. Download the image URL twice and save them into the wallpaper folder**
4. Create a Tkinter GUI to display a small window displaying the explanation
5. Create a CronJob to execure the process periodically.
  
** I came across a glitch where MacOS will refuse to cycle through a single image in a folder. Importing two images worked well instead. 
### CronJob 
`10 0 * * * ~/Documents/NASA-Wallpaper-Auto-Changer/bin/python3.9 ~/Documents/NASA-Wallpaper-Auto-Changer/main.py >> ~/Documents/NASA-Wallpaper-Auto-Changer/logfile.log 2>&1`
