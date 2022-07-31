import requests
import time
import os
 
if __name__ == "__main__":
      
    HOSTNAME = os.getenv("HOSTNAME")
    print(f"Address API: {HOSTNAME}")
    test_req1 = requests.get(f"http://{HOSTNAME}:3001/news?country=gr")
                      
    if test_req1.status_code != 200:
        print("News API check failed")
        exit(1)
    else:
        print("News API checked")                                                       
    test_req2 = requests.get(f"http://{HOSTNAME}:3001/weather?city=amsterdam")
    if test_req2.status_code != 200:
        print("Weather API check failed")
        exit(1)
    else:
        print("Weather API checked")
