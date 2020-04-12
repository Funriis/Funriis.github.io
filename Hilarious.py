# This program is meant to download a file from the internet
# and replace itself with the downloaded content
# and then run itself

import requests
from time import sleep
from os import system

# Downloads file from given url
def dwFile(url):
  fc = requests.get(url).content
  return fc

# Writes file with given content to the current working directory
def wFile(content):
  with open("Replacer.py", "wb") as file:
    print("Writing file from updated file 4...")
    file.write(content)
    file.close()

while True:
  wFile(dwFile("https://funriis.github.io/Hilarious.py"))
  sleep(60)
  system("Replacer.py")
