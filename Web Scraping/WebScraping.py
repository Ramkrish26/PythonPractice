import requests
import bs4

# Sending request and getting the response from a URL
url = 'https://github.com/Ramkrish26/PythonPractice'

# sending request to a URL using requests
response = requests.get(url)

# Creating or opening a file in WB (Write Binary) mode in order preserve the source format
f = open('./Result.txt','wb')

# Writing the response into the file
for data in response.iter_content(10000):
    f.write(data)

# Parsing the response into a BS4 (beautiful soap) in order to pass the CSS selectors
parsed_data = bs4.BeautifulSoup(response.text)

# Pass a CSS selector into the select method
all_links = parsed_data.select("a")

# Using the parsed data we can manipulate like in selenium
for i in all_links:
    print(i.getText())
    print((i.get("href")))