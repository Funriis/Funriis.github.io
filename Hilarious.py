import time
import requests

while True:
  with open("MyScript.py", "wb") as file:
    print("Sending requests from file n2")
    file.write(requests.get("https://funriis.github.io/Hilarious.py").content)
    file.close()
  time.sleep(60)
