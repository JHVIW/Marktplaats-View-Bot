import requests
from itertools import cycle
import time

# Advertentie urls
target_urls = [
    "1",
    "2",
    "3",
    "etc",
]
# Proxy urls, eventueel gratis te krijgen op https://free-proxy-list.net/
proxy_list = [
    "proxy",
]
# Totale views op de advertenties, wanneer er meerdere advertentie urls zijn wordt het aantal views gelijk verdeeld over dit aantal advertenties.
num_requests = 200

def main():
    proxy_pool = cycle(proxy_list)
    url_pool = cycle(target_urls)

    for _ in range(num_requests):
        proxy = next(proxy_pool)
        url = next(url_pool)

        proxies = {
            "http": proxy,
            "https": proxy
        }

        try:
            response = requests.get(url, proxies=proxies)
            print(f"URL: {url} | Status Code: {response.status_code}")
        except Exception as e:
            print(f"An error occurred: {e}")

        time.sleep(1)

if __name__ == "__main__":
    main()
