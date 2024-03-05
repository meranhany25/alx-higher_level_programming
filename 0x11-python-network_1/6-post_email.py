#!/usr/bin/python3
"""A  script that:
takes in a URL and an email address
sends a POST request to the passed URL with the email as a parameter
displays the body of the response.
"""

if __name__ == "__main__":
    import sys
    import requests
    url = sys.argv[1]
    email = sys.argv[2]
    r = requests.post(url, data={'email': email})
    print(r.text)
