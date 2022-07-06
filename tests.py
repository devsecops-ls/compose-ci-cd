import requests
import time

if __name__ == "__main__":
    test_req1 = requests.get("http://localhost/news?country=gr")

    if test_req1.status_code != 200:
        exit(1)
    else:
        print("News API checked")

    test_req2 = requests.get("http://localhost/weather?city=amsterdam")
    if test_req2.status_code != 200:
        exit(1)
    else:
        print("Weather API checked")
