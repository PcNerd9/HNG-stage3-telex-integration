import requests
from time import sleep



def send_incorrect_credentaials():
    url = "https://aylon.duckdns.org/login"
    data = {
        "email": "testing@gmail.com",
        "password": "testingg"
    }
    print("Sending incorrect credentials")
    for _ in range(5):
  
        response = requests.post(url, json=data)
        print(f"\tAttempt: {_ + 1} {response.json()}")
    response = requests.post(url, json=data)
    print(f"\tAttempt: 6 {response.json()}")



def send_incorrect_credentials_from_different_ip():
    url = "https://aylon.duckdns.org/login"
    data = {
        "email": "testing@gmail.com",
        "password": "testingg"}
    
    with open("ips.txt") as f:
        ip_addresses = f.read().splitlines()

        for i in range(5):
            response = requests.post(url, json=data, headers={"X-Forwarded-For": ip_addresses[i]})
            print(f"\tAttempt: {i + 1} {response.json()}")
        response = requests.post(url, json=data, headers={"X-Forwarded-For": ip_addresses[5]})
        print(f"\tAttempt: 6 {response.json()}")


def main():
    send_incorrect_credentaials()
    print("waiting for 5 minutes")
    sleep(300)
    send_incorrect_credentials_from_different_ip()

if __name__ == "__main__":
    main()