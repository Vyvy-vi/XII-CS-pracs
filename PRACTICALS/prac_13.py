"""
Use urllib3 module.
"""

import urllib3

http = urllib3.PoolManager()

res = http.request('GET', 'https://www.pythonforbeginners.com/')
head = res.info()

# Print Headers-
print(f"Headers - {head}")
# Print Date-
print(f"Date- {head['date']}")
# Print Server-
print(f"Server- {head['server']}")

print('Writing data…')
with open('downlaod.htm', 'w') as htm:
    htm.write(str(res.data))
