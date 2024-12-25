"""This module prints python version, path location and tries to perform get on coreyms website."""

import requests


print("Hello World!")
r = requests.get("https://coreyms.com", timeout=10)
print(r.status_code)
print(r.ok)
