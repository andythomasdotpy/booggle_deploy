import requests
from bs4 import BeautifulSoup
from .functions import search_to_url, slugify


# Takes user input and returns a dictionary with the results, the number of each result and an image link
def bot_find_search_results(user_input):

    # Convert search results to all lowercase
    user_input.lower()

    # Create url for search bot
    dynamic_url = search_to_url(user_input)

    # Headers Dictionary
    headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://google.com",
    "DNT": "1",
    }

    # Soupify data
    r = requests.get(dynamic_url, headers=headers)

    # Soupify data
    soup = BeautifulSoup(r.text, 'html.parser')

    gen_list = soup.select("div .views-row")
    num_bottles_returned = len(gen_list)

    outer_list = list()
    # Iterate through results and extract bottle name and sales status
    for index, item in enumerate(gen_list):
        inner_list_tmp = []
        bottle_name = item.find(class_="protitle").contents[0].lower()
        sales_status = item.find_all(class_="label")[1].contents[0]
        my_slug = slugify(bottle_name)


        # Extract image url
        link = item.find(class_="productimage")
        image_url = link.find("img")["src"]

        # Verify auction has ended
        if sales_status == "Winning Bid:":

            if len(outer_list) == 0:
                tmp_first_inner = list()
                tmp_first_inner.append(str(bottle_name.title()))
                tmp_first_inner.append(0)
                tmp_first_inner.append(image_url)
                tmp_first_inner.append(my_slug)
                outer_list.append(tmp_first_inner)

        for i, v in enumerate(outer_list):

            outer_list_len = len(outer_list)
            inner_list_tmp = list()

            if bottle_name.title() in v:
                v[1] += 1
                break

            if outer_list_len - 1 == i:
                inner_list_tmp.append(bottle_name.title())
                inner_list_tmp.append(1)
                inner_list_tmp.append(image_url)
                inner_list_tmp.append(my_slug)
                outer_list.append(inner_list_tmp)
                break

    return outer_list