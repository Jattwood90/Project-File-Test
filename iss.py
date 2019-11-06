from tkinter import *
import webbrowser
import requests
import json

#iss json and browser function
def iss():
    #api link
    url = ("http://api.open-notify.org/iss-now.json")

    #requests data as string
    r = requests.get(url).text

    #convert string to Json

    r = json.loads(r)
    location = r['iss_position']
    longitude = (location['longitude'])
    latitude = (location['latitude'])

    #opens result in google maps
    webbrowser.open(f"https://www.google.com/maps/search/?api=1&query={latitude},{longitude}")

#window prompt code using tkinter

root = Tk()

def close_window():
    root.destroy()

theLabel = Label(root, text=("Welcome to the ISS viewer! \n\n"
      "This programme will open up the current location in your browser with Googlemaps."
      "\n\n\nWould you like to continue?\n\n"))

theLabel.pack()

btn = Button(root, text = "Yes", command = iss)
btn.pack()

btnNo = Button(root, text = "No", command = close_window)
btnNo.pack()

root.mainloop()
