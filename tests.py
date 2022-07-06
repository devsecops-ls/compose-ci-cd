import requests
import time
import os

if __name__ == "__main__":

    # to get the IP: docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}'  compose-ci-cd_master_1
    IP_ADDRESS_API = os.getenv("IP_ADDRESS_API")
    test_req1 = requests.get("http://{IP_ADDRESS_API}:3001/news?country=gr")

    if test_req1.status_code != 200:
        exit(1)
    else:
        print("News API checked")

    test_req2 = requests.get("http://{IP_ADDRESS_API}:3001/weather?city=amsterdam")
    if test_req2.status_code != 200:
        exit(1)
    else:
        print("Weather API checked")
