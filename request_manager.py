import requests
from config import cookies, headers

session = requests.Session()

@staticmethod
def doRequest(url):
    request = session.get(url, headers=headers, cookies=cookies)
    if request.status_code == 200:
        return request.text
    else:
        print(f"Error doing request, status code: {request.status_code}")
        return ""