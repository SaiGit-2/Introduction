"""This module prints python version, path location and tries to perform get on coreyms website."""

import sys
import requests


print(sys.version)
print(sys.executable)
print("Hello World!")
r = requests.get("https://coreyms.com", timeout=10)
print(r.status_code)
