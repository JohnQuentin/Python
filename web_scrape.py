import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/" #difine the url
page = requests.get(URL) #use a HTTP get request to get the HTML data
soup = BeautifulSoup(page.content, "html.parser") #parsers it the right way
results = soup.find(id="ResultsContainer") #all the jobs are in <div id="ResultsContainer">

job_elements = results.find_all("div", class_="card-content") #assiging all div from card-content to variable

for job_element in job_elements:
    title_element = job_element.find("h2", class_="title") #assigning elements to variables
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip()) #text gives you only the text and strip removes the whitespace
    print(company_element.text.strip())
    print(location_element.text.strip())
    print() #new line after titel, company and location

