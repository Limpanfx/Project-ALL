import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import socks
import socket

# Load proxies from file
def load_proxies(file_name):
    with open(file_name, 'r') as f:
        return [line.strip() for line in f if line.strip()]

# Detect proxy type
def get_proxy_type(proxy):
    socks_ports = ['1080', '4145', '9050', '9051']
    if any(proxy.endswith(f":{port}") for port in socks_ports):
        return "socks5"  # Assume SOCKS5
    return "http"

# Set up proxy using PySocks (for SOCKS5 support)
def set_socks_proxy(proxy):
    ip, port = proxy.split(":")
    socks.set_default_proxy(socks.SOCKS5, ip, int(port))
    socket.socket = socks.socksocket  # Override default socket

# Set up WebDriver with proxy
def setup_driver(proxy):
    chrome_options = Options()
    proxy_type = get_proxy_type(proxy)

    if proxy_type == "socks5":
        set_socks_proxy(proxy)  # Configure SOCKS5 proxy properly
    else:
        chrome_options.add_argument(f'--proxy-server=http://{proxy}')

    chrome_options.add_argument("--headless")  
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=chrome_options)

# Visit website and click
def visit_website_with_proxy(proxy, website_url):
    try:
        driver = setup_driver(proxy)
        print(f"Using proxy {proxy} ({get_proxy_type(proxy)}) to visit {website_url}...")

        driver.get(website_url)
        time.sleep(random.uniform(3, 7))  

        for _ in range(3):  
            driver.find_element(By.TAG_NAME, 'body').click()
            time.sleep(random.uniform(1, 3))  

        print(f"✅ Successfully visited {website_url} using {proxy}")
    
    except Exception as e:
        print(f"❌ Error with proxy {proxy}: {e}")
    
    finally:
        driver.quit()

# Main function
def main():
    proxies = load_proxies("Proxies.txt")
    website_url = "https://www.guns.lol/Limpan"

    for proxy in proxies:
        visit_website_with_proxy(proxy, website_url)

if __name__ == "__main__":
    main()
