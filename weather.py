# pip install beautifulsoup4      8/8/2024 n0t worked but I learnt
# pip install requests
import requests
from bs4 import BeautifulSoup

city = input("Enter City Name:  ")
city_formated = city.lower().replace(" ", "-")

url = f"https://www.timeanddate.com/weather/Nigeria{city_formated}"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

try:
   temperature = soup.find("div", class_="span").get_text(strip=True)
   description = soup.find("div", class_="span").find_next("span").get_text(strip=True)

   print(f"Weather  {city}:")
   print(f"Temperature {temperature}:")
   print(f"Condition {description}:")

except AttributeError:
   print("Weather information could not be found.")   
   print(soup.prettify())  # Print the entire HTML structure for inspection
# print(soup.prettify()) is a valuable tool for understanding and debugging your web scraping code.