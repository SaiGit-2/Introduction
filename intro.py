"""This module prints python version, path location and tries to perform get on yahoo website."""

import requests


print("Hello World!")
r = requests.get("https://yahoo.com", timeout=10)
print(r.status_code)
print(r.ok)
