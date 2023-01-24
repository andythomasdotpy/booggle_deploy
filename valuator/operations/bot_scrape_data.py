import datetime
import requests
from bs4 import BeautifulSoup
from .functions import search_to_url, name_filter_auto

# Take user input and return all resulsts that match
def bottle_results_bot(bottle_input):

    x_rate = 1.22

    # Convert search results to all lowercase
    bottle_input.lower()

    # Create url for search bot by calling "search_to_url" function in file called "functions"
    dynamic_url = search_to_url(bottle_input)

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

    main_list = list()
    for index, item in enumerate(gen_list):
        bottle_name_new = item.find(class_="protitle").contents[0].lower()
        sales_status = item.find_all(class_="label")[1].contents[0]

        # Extract image url
        link = item.find(class_="productimage")
        image_url = link.find("img")["src"]


        #Create temp list for each row
        row = []

        # Verify if bottle scraped matches user requested bottle by calling "name_filter_auto" function in file called "functions"
        bool_filter = name_filter_auto(bottle_name_new, bottle_input)

        # Only add bottles that pass the filter (if filter activiated)
        if bool_filter == True:

            # Only include bottles if auction has closed "Winning Bid:" status means auction has closed
            if sales_status == "Winning Bid:":
                # Create a list called "price_list" will pull the price and sale date and insert into a list
                price_list = item.find_all(class_="uc-price")

                # Extract price from list and assign to varible "raw_price"
                raw_price = price_list[0].contents[0][1:]

                # Remove comma's from price
                price_usd = raw_price.replace(",", "")

                # Convert price from string to int and convert from pounds to dollars
                price_int = int(int(price_usd) * x_rate)

                # Convert price to string and add "$"
                price_final_str = "$"
                price_final_str += str(price_int)

                # Extract date from list and assign to variable "sales_date"
                sales_date = price_list[1].contents[0]

                # Convert date from string to datetime object
                date_time_obj = datetime.datetime.strptime(sales_date, '%d.%m.%y').strftime("%b %d, %Y")

                # Add all the variables to a temp list called "row"
                row.append(bottle_name_new.title())
                row.append(price_final_str)
                row.append(date_time_obj)
                row.append(image_url)

                # Add row to csv file
                main_list.append(row)

    return main_list