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
        "http://ddockkkwl45kmnnd7b332qu4h3ov66e3zy2ytrpfarpswvtldcx3cvad.onion/",

    ]




    session = requests.session()
    session.proxies = {'http': 'socks5h://localhost:9050', 'https': 'socks5h://localhost:9050'}

    for url in urls:
        status = test_connection(url, session)
        print(f"{url} {status}")
