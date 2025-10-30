import requests

url = "https://country-leaders.onrender.com/leaders?country=fr"  # change to "ma" to test Morocco
cookie_url='https://country-leaders.onrender.com/cookie'
cookies=requests.get(f"{cookie_url}")
cookies=cookies.cookies
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",}

try:
    response = requests.get(url, headers=headers, timeout=10,cookies=cookies)
    print("Status code:", response.status_code)
    print("Response headers:", response.headers)
    if response.status_code == 200:
        print("Data:", response.json())
    else:
        print("Body:", response.text)
except requests.exceptions.RequestException as e:
    print("Error:", e)