from email import header
from bs4 import BeautifulSoup
import re
import requests
from scraper.leader import Leader 

class CountryScraper:
    def __init__(self):
        self.root_url='https://country-leaders.onrender.com'
        self.cookie_url = f"{self.root_url}/cookie"
        self.countries_url = f"{self.root_url}/countries"
        self.leaders_url = f"{self.root_url}/leaders"
        self.cookie=None

    def _get_cookie(self):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) ..."}
        resp=requests.get(f"{self.cookie_url}",headers=headers) #this variable will hold the HTTP response object
        resp.raise_for_status() #checks the HTTP response's status code- does nothing if 200-299, if there's an error it raises a requests.HTTPerror exception
        self.cookies={"user_cookie": resp.cookies.get("user_cookie")}
        return self.cookies
    
    def _fetch_url(self,url):
        cookies=self._get_cookie()
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) ..."}
        response= requests.get(url, cookies=cookies, headers=headers)
        response.raise_for_status()
        return response

    def get_countries(self):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) ..."}
        url=self.countries_url
        cookies=self._get_cookie()
        response=requests.get(url, cookies=cookies,headers=headers)
        response.raise_for_status()
        self.countries=response.json()
        return self.countries

    def get_leaders(self):
        import time
        session = requests.Session()
        url = self.leaders_url
        countries = self.get_countries()
        cookies = self._get_cookie()
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) ..."}
        self.leaders_per_country = {}
        self.leaders=[]

        for country in countries:
            print(f"Fetching leaders for {country}...")
            self.retry_attempt = 0
            while self.retry_attempt < 3:
                try:
                    response = requests.get(url, params={"country": country}, cookies=cookies, headers=headers)
                    response.raise_for_status()
                    print(f"Raw JSON for {country}:", response.json())
                    leaders = response.json()

                    if isinstance(leaders, dict) and "message" in leaders and "expired" in leaders["message"].lower():
                        print(f"Cookie expired for {country}, refreshing...")
                        cookies = self._get_cookie()
                        self.retry_attempt += 1
                        continue

                    for leader in leaders:
                        wiki_url = leader.get("wikipedia_url")
                        name = leader.get("name")
                        if wiki_url:
                            print(f"  Processing {leader}...")
                            leader_obj = Leader(name, wiki_url)
                            leader_obj.get_first_paragraph(session, do_clean_paragraph=True)
                            leader["first_paragraph"] = leader_obj.first_paragraph
                            time.sleep(0.2)

                    self.leaders_per_country[country] = leaders
                    print(f"Successfully fetched leaders for {country}.")
                    break  # success, break retry loop

                except (requests.RequestException, ValueError) as e:
                    print(f"Error fetching leaders for {country}: {e}")
                    self.leaders_per_country[country] = []
                    self.retry_attempt += 1
                    time.sleep(0.5)

        return self.leaders_per_country

        
                
