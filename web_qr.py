# -*- coding: utf-8 -*-
"""Untitled

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XsfgOW2VzqsmUieJWoXMJguSLGhh3Z4H
"""

import qrcode
import urllib


http_status_codes = {
    100: "Continue",
    200: "OK",
    201: "Created",
    204: "No Content",
    301: "Moved Permanently",
    302: "Found",
    304: "Not Modified",
    400: "Bad Request",
    401: "Unauthorized",
    404: "Not Found",
    500: "Internal Server Error",
    502: "Bad Gateway",
    503: "Service Unavailable"
}


print('Checking connectivity : ')
url = 'https://google.com'
response = urllib.request.urlopen(url)
print(f'The respond code was {response.getcode()} {http_status_codes[response.getcode()]}')

create = input('make qrcode? (Y/N)')

if create == 'Y':
  img = qrcode.make(url)
  img.save('image.jpg')