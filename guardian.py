import requests
import csv
import json

"""This script is designed to open the JSON data from the Guardian's developer API, and save it into a CSV file.
A use for this could be to save headlines, over the course of a period, and conduct a
discourse analysis of the language used."""

"""TODO: look into wayback machine, or previous headline entries, as an option to scrape previous published data"""


#This key can be obtained for free, via the Guardian's developer web-page
url_key = "https://content.guardianapis.com/search?api-key=51ea78b1-e8a4-4331-9ea5-7eadf4c4ca48"


#Json loading of data
r = requests.get(url_key).text
r = json.loads(r)

response = r['response']
results = response['results']


#CSV writer
with open('C:\\Users\\Joe\\Desktop\\test.csv', 'w', newline='') as csv_file:

    fields = ['webTitle', 'webPublicationDate',
              'webUrl','apiUrl', 'type', 'sectionId',
              'isHosted', 'pillarName', 'sectionName', 'pillarId', 'id']

    writer = csv.DictWriter(csv_file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(results)

print("Printing complete")

csv_file.close()

