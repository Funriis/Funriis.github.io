import time
import requests

while True:
  with open("MyScript.py", "wb") as file:
    file.write(requests.get("https://funriis.github.io/Hilarious.py").content)
    file.close()
  time.sleep(600)
