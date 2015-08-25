#!/usr/bin/env python

import os
import sqlite3

import requests


SCHEMA = """
  create table inscription (
    rch INTEGER PRIMARY KEY,
    page TEXT
    );
"""

def connect(fname):

    if os.path.exists(fname):
        conn = sqlite3.connect(fname)
        return conn

    conn = sqlite3.connect(fname)
    conn.execute(SCHEMA)
    conn.commit()
    return conn


# req = requests.post("http://suivi.paris-brest-paris.org/index.php", data={"rch":"1", "rch_num":"5", "rch_nom":""})
# req = requests.post("http://suivi.paris-brest-paris.org/index.php", data={"rch":"1", "rch_num":"5"})
# import pdb; pdb.set_trace()

def main():
    conn = connect("pbp2015.sqlite")
    cursor = conn.cursor()

    for rch in range(6):
        req = requests.post("http://suivi.paris-brest-paris.org/index.php", data={"rch":"1", "rch_num":"5"})
        if req.status_code == 200:
            try:
                cursor.execute("insert into inscription values (?, ?)", (rch, unicode(req.content, "utf8")))
            except Exception:
                import pdb; pdb.set_trace()
                pass
            conn.commit()


if __name__ == "__main__":
    main()
