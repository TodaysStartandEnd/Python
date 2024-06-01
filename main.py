## WebScraper2 - BeautifulSoup(html parsing library)
import requests
from bs4 import BeautifulSoup

url = "https://nomadcoders.co/courses"

response = requests.get(url)
##print(response.content)

soup = BeautifulSoup(response.content, 'html.parser')
nomadcourse_name = soup.find('div',class_="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-y-5 gap-x-10 pb-10").find_all('h3')


print(nomadcourse_name)