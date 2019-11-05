import webbrowser
import requests
import json
import click

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

#Prompt

print("Welcome to the ISS viewer! \n"
      "This programme will open up the current location in your browser with Googlemaps."
      "\nWould you like to continue?")

if click.confirm('Yes or no?', default=True):
    iss()
else:
    print("No selected. Goodbye")