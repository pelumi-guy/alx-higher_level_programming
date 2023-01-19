#!/usr/bin/python3
"""
a Python script that fetches
https://alx-intranet.hbtn.io/status
"""
import urllib.request


if __name__ == '__main__':
    with urllib.request.urlopen(
            'https://alx-intranet.hbtn.io/status') as response:
        body = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(body)))
        print('\t- content: {}'.format(body))
        print('\t- utf8 content: {}'.format(str(body, 'UTF-8')))