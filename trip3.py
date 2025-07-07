from IPython.core.display import display_pretty
from helpers import display_table, get_llm_response, read_csv

itinerary = []

# read cvs file
itinerary = read_csv("itinerary2.csv")
# show pretty output
display_table(itinerary)

detailed_itinerary = {}

 # Use the 'for' loop over the 'itinerary' list
for trip_stop in itinerary:
    city = trip_stop["City"]
    country = trip_stop["Country"]
    arrival = trip_stop["Arrival"]
    departure = trip_stop["Departure"]

    rest_dict = read_csv(f"{city}.csv")

    print(f"Creating detailed itinerary for {city}, {country}.")

    prompt = f"""I will visit {city}, {country} from {arrival} to {departure}.
        Please note the City on the top and create a daily itinerary with detailed activities.
        Designate times for breakfast, lunch, and dinner.

        I want to visit the restaurants listed in the restaurant dictionary without repeating any place.
        Make sure to mention the specialty that I should try at each of them.

        Restaurant dictionary:
        {rest_dict}

        """
    # Store the detailed itinerary for the city to the dictionary
    detailed_itinerary[city] = get_llm_response(prompt)

display_pretty(detailed_itinerary["New York"])
