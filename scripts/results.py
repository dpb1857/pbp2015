#!/usr/bin/env python

import json
import time

import requests

CONTROLS = [
 "START",
#  "MORTAGNE",
 "VILLAINES",
 "FOUGERES",
 "TINTENIAC",
 "LOUDEAC",
 "CARHAIX",
 "BREST",
 "CARHAIX2",
 "LOUDEAC2",
 "TINTENIAC2",
 "FOUGERES2",
 "VILLAINES2",
 "MORTAGNE2",
 "DREUX2",
 "FINISH"
 ]

DISTANCES = [0, 221, 310, 364, 449, 525, 618, 703, 782, 867, 921, 1009, 1090, 1165, 1230]


def delta_t(t, t0):
    t_parts = t.split(':')
    t0_parts = t0.split(':')
    total_minutes = int(t_parts[0])*60 + int(t_parts[1]) - (int(t0_parts[0])*60 + int(t0_parts[1]))
    hrs = total_minutes/60
    mins = total_minutes % 60
    return "{:02d}:{:02d}".format(hrs, mins)


def get_results(frame):

    req = requests.get("http://suivi.paris-brest-paris.org/data/{}.txt".format(frame))
    if req.status_code != 200:
        return []

    return req.content.split(';')

if False:
    # data = requests.get("http://suivi.paris-brest-paris.org/data/X169.txt").content

    data = requests.get("http://suivi.paris-brest-paris.org/data/Z095.txt").content

    times = data.split(';')
    info = zip(CONTROLS, times)

    start = times[0]
    for i, t in enumerate(times):
        print i, CONTROLS[i], DISTANCES[i], delta_t(t, start)


def main():

    import sys

    riders = sys.argv[1]
    with open(riders) as f:
        for line in f:
            data = json.loads(line)
            plaque = data["plaque"]
            print json.dumps({"plaque":plaque, "results":get_results(plaque)})
            time.sleep(0.1)
if __name__ == "__main__":
    main()
