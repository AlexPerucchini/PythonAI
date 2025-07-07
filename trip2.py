from IPython.core.display import display_pretty
from helpers import display_table, get_llm_response, read_csv, read_txt

itinerary = []

itinerary = read_csv("itinerary.csv")
# show pretty output
display_table(itinerary)

print("********************************************************************************************")
# read txt file
journal = read_txt("Sydney.txt")
print(journal)
print("********************************************************************************************")

# read cvs file
sydney_restaurants = read_csv("Sydney.csv")
display_table(sydney_restaurants)
print("********************************************************************************************")
stop_in_sydney = itinerary[6]
arrival = stop_in_sydney["Arrival"]
departure = stop_in_sydney["Departure"]
city = stop_in_sydney["City"]
country = stop_in_sydney["Country"]

# Write the prompt
prompt = f"""I will visit {city}, {country} from {arrival} to {departure}.
Create a daily itinerary with detailed activities.
Designate times for breakfast, lunch, and dinner.

I want to visit the restaurants listed in the restaurant dictionary
without repeating any place. Make sure to mention the specialty
that I should try at each of them.

Restaurant dictionary:
{sydney_restaurants}
"""
r = get_llm_response(prompt)
#pprint.pprint(r)
display_pretty(r)
