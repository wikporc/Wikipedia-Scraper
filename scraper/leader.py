
from bs4 import BeautifulSoup
import re
import requests
import time

class Leader:
    patterns=[r"\[\d+\]", #references like [42]
            r"<span.*?>.*?</span>", #<span> blocks - phonetic buttons, styling
            r"\([^\)]*\)", #phonetic pronunciations
            r"[\u2460-\u24FF]", # Extra unicode symbols like ⓘ etc
            r"<.*?>" #HTML tags (if there are any)
            ]#this is a list that contains all the regex patterns to remove from the text for cleaning

    def __init__ (self,name,wikipedia_url):
        self.name=name
        self.wikipedia_url=wikipedia_url
        self.first_paragraph=None

    def get_first_paragraph(self,session,do_clean_paragraph=True):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) ..."}
        html_text = session.get(self.wikipedia_url, headers=headers).text
        soup = BeautifulSoup(html_text, "html.parser")
        for paragraph in soup.find_all("p"):
            if paragraph.find("b")==paragraph.contents[0]: #checks if our <p> element starts with bold <b> text.
                first_paragraph=paragraph.get_text()
                if do_clean_paragraph:
                    self.first_paragraph=self.clean_paragraph(first_paragraph)
                else:
                    return first_paragraph

            
            
    def clean_paragraph(self,text):
        for pattern in self.patterns: #made a loop here to see the effects of each applied regex pattern for testing
            text= re.sub(pattern,"",text,flags=re.DOTALL) #the flag makes it detect things through new lines (/n)
        return text


    
   