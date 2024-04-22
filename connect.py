import requests
from urllib.parse import urlparse

def test_connection(url, session):
    try:
        response = session.head(url)  # Using HEAD to minimize data transfer
        response.raise_for_status()  # Raise an exception for HTTP errors
        return "✅"
    except requests.RequestException:
        return "❌"

if __name__ == "__main__":
    urls = [
        "http://ransomocmou6mnbquqz44ewosbkjk3o5qjsl3orawojexfook2j7esad.onion/",

    ]




    session = requests.session()
    session.proxies = {'http': 'socks5h://localhost:9050', 'https': 'socks5h://localhost:9050'}

    for url in urls:
        status = test_connection(url, session)
        print(f"{url} {status}")
