
import requests
from bs4 import BeautifulSoup
import pandas as pd
# Scrape the Books to scrap website
# Get book: title, stars, price, link, number in stock

# 1. Decided what webpage to webscrape 
# 2. Download and import 



def main():
    url = "https://books.toscrape.com/catalogue/category/books_1/index.html"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    books_data = []
    # Get all products
    products = soup.find_all(class_="product_pod")
    for product in products:
        # Get title
        title = product.find('h3').find('a')['title']
        
        # Get rating
        rating = product.find('p')['class'][1] + " Stars"

        # Get price
        price = product.find(class_="price_color").get_text(strip=True)
        price = price.split("£")[1]

        # Get link
        link = product.find('h3').find('a')['href']
        url = "https://books.toscrape.com/catalogue/category/books_1/" + link

        # Get number in stock
        stock = product.find(class_="instock availability").get_text(strip=True)

        # Find the number in stock
        if stock == "In stock":
            number_in_stock = get_stock_number(url)
        else:
            number_in_stock = 0

        print()
        print("Title:\t", title)
        print("Rating:\t", rating)
        print("Price:\t", "£" + price)
        print("Link:\t", url)
        print("Stock:\t", number_in_stock)

        books_data.append({
            "Title": title,
            "Rating (out of Five)": rating,
            "Price (in pounds)": price,
            "Link": url,
            "Stock": number_in_stock
        })

    # Save data to CSV
    data_to_csv(books_data)



def get_stock_number(url):
    """
    Retrieves the stock number from a given URL.
    Args:
        url (str): The URL of the webpage to scrape.
    Returns:
        int: The stock number.
    """

    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the element with class "instock availability" and get its text
    stock = soup.find(class_="instock availability").get_text(strip=True)

    # Extract the stock number from the text
    stock_number = int(stock.split()[2].strip("("))

    # Return the stock number
    return stock_number


def data_to_csv(books_data):
    """
    Saves the data to a CSV file.
    Args:
        books_data (list): A list of dictionaries containing the data to save.
    """

    # Create a Pandas DataFrame from the list of dictionaries
    df = pd.DataFrame(books_data)

    # Save the DataFrame to a CSV file
    df.to_csv("books.csv", index=False)


if __name__ == "__main__":
    main()