#requests library: fetch the web page content.
import requests

#BeautifulSoup from the bs4 library to parse the HTML.
from bs4 import BeautifulSoup

Url = 'https://www.cnbc.com/site-map/'

response = requests.get(Url)

if response.status_code == 200:
    print("Page successfully fetched")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")

#Parse the HTML content  
beautifulSoup = BeautifulSoup(response.content, 'html.parser')

#make it readable
print(beautifulSoup.prettify())

#extract headings
heading_tag = beautifulSoup.find('h1')
if heading_tag is not None:
    heading = heading_tag.text
    print(f"Heading: {heading}")
else:
    print("No <h1> tag found")
#extract links
links = beautifulSoup.find_all('a')
if links:
    for link in links:
        href = link.get('href')
        if href:
            print(href)
else:
    print("No <a> tags found")

#save the data into a file
with open('output.txt', 'w') as f:
    if heading_tag is not None:
        f.write(f"Heading: {heading}\n")
    else:
        f.write("No <h1> tag found\n")
    
    for link in links:
        href = link.get('href')
        if href:
            f.write(f"{href}\n")




