#!/usr/bin/env python

import json
import os
import time

from lxml import html
import requests


def main():

    for rch in range(1, 8000):
        req = requests.post("http://suivi.paris-brest-paris.org/index.php", data={"rch":"1", "rch_num":rch})
        if req.status_code == 200:
            tree = html.document_fromstring(req.content)
            try:
                lastname, firstname, plaque = [element.text for element in tree.xpath("//table[2]/tr[2]/td")]
            except Exception:
                continue
            print json.dumps({"rch": rch, "lastname":lastname, "firstname": firstname, "plaque": plaque})
            time.sleep(0.25)

if __name__ == "__main__":
    main()
