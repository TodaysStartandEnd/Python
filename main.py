## WebScraper3 - BeautifulSoup(html parsing library) : extraction text
import requests
from bs4 import BeautifulSoup

url = "https://nomadcoders.co/courses"

response = requests.get(url)
##print(response.content)

soup = BeautifulSoup(response.content, 'html.parser')
nomadcourse_names = soup.find('div',class_="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-y-5 gap-x-10 pb-10")

idx = 1;
for name in nomadcourse_names :
  title = name.find("h3", class_ ="text-xl overflow-hidden").text
  print("-----------------------------------------------")
  print(idx," ",title)
  idx += 1
  



