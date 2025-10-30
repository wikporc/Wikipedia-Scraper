import json
from scraper.leader import Leader
def save(leaders_per_country):
    with open('leaders_output.json', 'w') as f:
        json.dump(leaders_per_country, f)