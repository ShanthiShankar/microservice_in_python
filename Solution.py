import requests
from bs4 import BeautifulSoup
from collections import Counter
import json

def count_words(url):
   
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.get_text()
    words = text.split()
    word_count = Counter(words)
    json_output = json.dumps(word_count, indent=4)
    return json_output