import requests
import random
import time

def load_proxies(filename):
    """Läser in proxyservrar från en fil och returnerar en lista."""
    with open(filename, 'r') as file:
        proxies = [line.strip() for line in file.readlines() if line.strip()]
    return proxies

def get_proxy_dict(proxy):
    """Skapar en proxy-dictionary för requests-biblioteket."""
    return {"http": proxy, "https": proxy}

def make_request(url, proxies):
    """Gör en webbförfrågan genom en slumpmässig proxy."""
    proxy = random.choice(proxies)
    proxy_dict = get_proxy_dict(proxy)
    try:
        response = requests.get(url, proxies=proxy_dict, timeout=5)
        print(f"Proxy: {proxy} | Status: {response.status_code}")
        return response.text
    except requests.RequestException as e:
        print(f"Fel med proxy {proxy}: {e}")
        return None

if __name__ == "__main__":
    proxy_file = "proxy.txt"  # Fil med proxies (en per rad)
    test_url = "http://httpbin.org/ip"  # Testar att hämta IP
    
    proxies = load_proxies(proxy_file)
    if not proxies:
        print("Ingen proxy hittades!")
    else:
        for _ in range(5):  # Testa 5 gånger med olika proxies
            make_request(test_url, proxies)
            time.sleep(2)  # Vänta lite mellan förfrågningar
