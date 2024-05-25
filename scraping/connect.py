import requests

""" Function test_con() takes the URL specified att retrieves its head element from the session, that is connected 
through socks5h proxy in order to access the TOR network. HTTP in the URL is used instead of HTTPS due to the specific website's operations. """
def test_con(url, session):
    try:
        response = session.head(url)
        response.raise_for_status()
        return "✅"
    except requests.RequestException:
        return "❌"


if __name__ == "__main__":
    session = requests.session()
    session.proxies = {'http': 'socks5h://localhost:9050', 'https': 'socks5h://localhost:9050'}

    url = "http://oirolrkrppy6sei6x6bvkkdolc4cjqzqfhxisfzu6exqblahwrrvktyd.onion"
    status = test_con(url, session)
    print(f"{url} {status}")
