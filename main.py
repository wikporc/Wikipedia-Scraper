# import the requests library (1 line)
import requests
import re
from bs4 import BeautifulSoup
from scraper.country_scraper import CountryScraper 
from scraper.leader import Leader
from scraper.utils import save
import time
scraper=CountryScraper()
leaders_per_country=scraper.get_leaders()
save(leaders_per_country)
 