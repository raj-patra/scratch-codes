__author__ = "Raj Patra"
__date__ = "26-07-2021"

import requests
from urllib.parse import urlencode
import sys    


def tinify():
    url = sys.argv[1:][0]
    request_url = "http://tinyurl.com/api-create.php?" + urlencode({"url": url})
    result = requests.get(request_url)
    print(result.text)

if __name__ == "__main__":
    tinify()