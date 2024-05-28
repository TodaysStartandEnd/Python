## Package 
## In pypi.org, you can find various packages that you can use in your code.
## replit.com is a website that allows you to load various packages via the cubic package button on the toolbar next to it.

from requests import get

website = "https://www.google.com"
response = get(website)
print(response) ##<Response [200]>
print(response.status_code) ##200
