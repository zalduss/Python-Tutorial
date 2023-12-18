import requests
import pandas as pd
from bs4 import BeautifulSoup


def check_from(price_text):

    if "From" in price_text:
        price = float(price_text.split("$")[1])
        return price
        

# URL of the website
url = "https://ikonick.com/collections/best-sellers"

# Send a GET request to the URL
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")

# with open("output.html", 'w', encoding="utf-8") as file:
    # file.write(soup.prettify())

with open("output.html", 'r', encoding="utf-8") as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, "html.parser")

# Find all Best Seller Products
products = soup.find_all(class_="column")

product_list = []

count = 1
for product in products:
    # Get link and product name
    # Name
    product_element = product.find('a', class_="product-card-title")
    # product_name = product_element['title']
    product_name = product_element.get_text(strip=True)
    # Link
    link = product_element['href']
    url = "https://ikonick.com" + link

    # Get Price
    price_element = product.find('span', class_="amount")
    price_text = price_element.get_text(strip=True)

    price = check_from(price_text)
    price = f"{price:.2f}"

    print()
    print("Product #", count)
    print("Name:", product_name)
    print(f"Cost: ${price}")
    print("Link:", url)
    count+=1

    product_list.append({
        "Name": product_name,
        "Price": price,
        "Link": url
    })

dataframe = pd.DataFrame(product_list)

dataframe.to_csv("ikonick.csv", index=False)





