from decouple import config
import requests


# Convert search term to url dynamically
def search_to_url(search):
    # Split search string into seperate words
    search_spliced = search.split()

    # Length of string
    length_search_splice = len(search_spliced)

    # Declare empty variable string for new url
    raw_url_bridge_beg = ""

    # Loop through each word and concatenate to empty string variable declared in previous step
    for i, word in enumerate(search_spliced):
        # If not last word in search string, add lowercased word to string and a plus afterwards
        if i != (length_search_splice - 1):
            raw_url_bridge_beg += word.lower() + "+"
        # If is last word, add only lowercased word to string wihthout +
        else:
            raw_url_bridge_beg += word.lower()

    raw_url_start = config("RAW_URL_START")
    raw_url_bridge_final = raw_url_bridge_beg
    raw_url_end = config("RAW_URL_END")

    # Concatenate start, string variable we created and end of url to final url and return to bottle_bot.py 
    final_url = raw_url_start + raw_url_bridge_final + raw_url_end

    return final_url


# Check if scrapped bottle matches users requested search criteria
def name_filter_auto(bottle_search, bottle_input_new):
    if bottle_search.title() == bottle_input_new:
        return True
    else:
        return False


def slugify(text):
    slug = ""
    for letter in text.lower():
        if letter.isalnum():
            slug += letter
        elif letter == " ":
            slug += "+"
    return slug


def convert():
    endpoint = "https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/gbp.json"
    response = requests.get(endpoint)
    data = response.json()
    print(data["gbp"]["usdt"])
    return data["gbp"]["usdt"]


