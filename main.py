## WebScraper1 - request content
## python can retrieve the content of the corresponding URL through the response to the request response. 
import requests

url = "https://www.naver.com"

response = requests.get(url)
print(response.content)

