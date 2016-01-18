#!/usr/bin/env python


import json
import os
import time

from lxml import html
import requests


FIELDS = ("time", "plaque", "lastname", "firstname", "country", "gender", "velo", "club")

def main():

    req = requests.get("http://www.paris-brest-paris.org/index2.php?lang=en&cat=presentation&page=resultats_2015")
    if req.status_code == 200:
        tree = html.document_fromstring(req.content)
        tables = tree.xpath("//table")
        for row in tables[0].xpath("//tr")[5:]:
            data = dict(zip(FIELDS, [td.text for td in row]))
            if data["plaque"] is None:
                break
            print json.dumps(data)

if __name__ == "__main__":
    main()
