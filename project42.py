
# Importing the urllib request, parse, and error modules
import urllib.request, urllib.parse, urllib.error
# Importing BeautifulSoup module
from bs4 import BeautifulSoup

# Asking for input from user. URL link.
url = input('Enter>> ')

# Variable html stores the urllib.request with urlopen(url).read()
html = urllib.request.urlopen(url).read()
# Creates the soup of html with the html variable. The 'html.parser' is the format for what kind of soup.  
soup = BeautifulSoup(html, 'html.parser')

# Variable tags set to the 'a' tags in the soup
tags = soup('a')
# Goes through the tags variable and prints the result
for tag in tags: 
    print(tag.get('href', None))