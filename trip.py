from prettytable import PrettyTable
from IPython.display import Markdown, display
import ollama
import pprint
import csv


model ='gemma2:2b'
prompt = ''
itinerary = []
response = ''

f = open("itinerary.csv", 'r')
csv_reader = csv.DictReader(f)

for row in csv_reader:
    itinerary.append(row)
f.close()

#create a better output for the itinerary
table = PrettyTable()

if itinerary:
    table.field_names = itinerary[0].keys() #set column headers
    for row_dict in itinerary:
        table.add_row(row_dict.values()) #set rows
print(table)

trip_stop = itinerary[0]
print("**************************************************************************")
print(trip_stop)
city = trip_stop["City"]
country = trip_stop["Country"]
arrival = trip_stop["Arrival"]
departure = trip_stop["Departure"]
print("**************************************************************************")
prompt = f"""I will visit {city}, {country}, from {arrival} to {departure}.
Please create a detailed daily itinerary."""
print("Please wait while I generate your trip information...")
response = ollama.generate(model, prompt)
pprint.pprint(response['response'])
print("**************************************************************************")
