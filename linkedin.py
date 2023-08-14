import requests
from bs4 import BeautifulSoup

# Replace this with the URL of the webpage you want to scrape
url = "https://www.linkedin.com/in/varunthammineni/"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Example: Extract and print the title of the webpage
    title = soup.title.string.strip()
    print("Title:", title)
    
    # Example: Extract and print all paragraph text from the page
    paragraphs = soup.find_all('p')
    for p in paragraphs:
        print("Paragraph:", p.get_text())
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
