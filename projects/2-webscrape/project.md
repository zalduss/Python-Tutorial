# Web Scraping Project Instructions

## Introduction
In this project, you will develop a Python script to scrape data from a book retail website. Your task is to extract details about books such as titles, ratings, prices, links, and stock numbers.

## Objectives
- Scrape data from a book retail website.
- Extract information including the book title, star rating, price, link, and number of books in stock.
- Save the extracted data into a CSV file.

## Required Libraries
- `requests`: To perform HTTP requests.
- `BeautifulSoup` from `bs4`: To parse and extract data from HTML.
- `pandas`: To organize data and save it in CSV format.

## Functions to Implement
1. **`main()`**: The main function to control the web scraping process.
2. **`get_stock_number(url)`**: Retrieves the number of books in stock from a book's detail page.
3. **`data_to_csv(books_data)`**: Saves the scraped data into a CSV file.

## Steps to Complete the Project
1. **Setup and Preparation**:
   - Install the required libraries:
     ```bash
     pip install requests beautifulsoup4 pandas
     ```

2. **Define the URL**:
   - Set the URL of the book retail website to be scraped.

3. **HTTP Request**:
   - Use `requests` to send a GET request to the website.

4. **Parse HTML Content**:
   - Use `BeautifulSoup` to parse the HTML content from the response.

5. **Extract Data**:
   - Extract the required information (title, rating, price, link, and stock number) for each book.
   - Store the data in a dictionary.

6. **Aggregate Data**:
   - Collect all book data dictionaries into a list.

7. **Save Data to CSV**:
   - Use `pandas` to convert the list of dictionaries into a DataFrame.
   - Export the DataFrame to a CSV file.

8. **Run and Test**:
   - Execute the script and check the CSV file to ensure the data is correct.

## Best Practices
- Inspect the HTML structure of the target website to understand the data layout.
- Use appropriate BeautifulSoup methods for data extraction.
- Handle exceptions and errors in HTTP requests.
- Ensure data is correctly formatted before saving to CSV.

## Deliverables
- A Python script that performs web scraping and saves data into a CSV file.
- The output CSV file containing the scraped data.

---
"""

# Writing the instructions to a Markdown file
md_file_path = '/mnt/data/web_scraping_project_instructions.md'
with open(md_file_path, 'w') as file:
    file.write(md_instructions)

md_file_path

