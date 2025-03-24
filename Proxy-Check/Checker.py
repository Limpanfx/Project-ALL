import requests

def check_proxy(proxy):
    # Format proxy string as dictionary for requests
    proxies = {
        "http": f"http://{proxy}",
        "https": f"https://{proxy}",
    }
    try:
        # Make a test request to check the proxy
        response = requests.get("https://www.example.com", proxies=proxies, timeout=10)
        
        # If status code is 200, the proxy works
        if response.status_code == 200:
            print(f"Proxy {proxy} is working.")
        else:
            print(f"Proxy {proxy} failed with status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Proxy {proxy} failed. Error: {e}")

def validate_proxies(filename):
    try:
        with open(filename, 'r') as file:
            proxies = file.readlines()
        
        # Check each proxy
        for proxy in proxies:
            proxy = proxy.strip()  # Remove leading/trailing spaces and newlines
            if proxy:  # Check if proxy is not empty
                check_proxy(proxy)
    except FileNotFoundError:
        print("The file proxies.txt was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the script with the 'proxies.txt' file
validate_proxies("proxies.txt")
