
# Find pylint codes at: http://pylint-messages.wikidot.com/all-codes
# pylint: disable=line-too-long
# pylint: disable=invalid-name
# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
# pylint: disable=superfluous-parens

# To use:
#
#   manage.py shell
#   from data import util
#   util.load_all()


import json

from django.db import transaction

from data.models import Rider, Control, Timestamp

def load_rider_data():
    f = open("../data/finalresults.json")
    count = 0
    with transaction.atomic():
        for record in f:
            r = json.loads(record)
            r["startgroup"] = r["plaque"][0]
            r = Rider(**r)
            r.save()
            count += 1

    print("Added {} Rider records".format(count))


locations = [(1, "SQY", 0, False),
             (2, "Vilaines-la-Juhel", 136, False),
             (3, "Fougeres", 191, False),
             (4, "Tinteniac", 224, False),
             (5, "Loudeac", 277, False),
             (6, "St-Nicholas-du-Pelem", 305, False),
             (7, "Carhaix", 327, False),
             (8, "Brest", 381, False),
             (7, "Carhaix", 434, True),
             (9, "Mael-Carhaix", 440, True),
             (5, "Loudeac", 486, True),
             (4, "Tinteniac", 539, True),
             (3, "Fougeres", 572, True),
             (2, "Vilaines-la-Juhel", 627, True),
             (10, "Mortagne-au-Perche", 678, True),
             (11, "Dreux", 726, True),
             (1, "SQY", 765, True)]

def load_control_locations():
    count = 0
    with transaction.atomic():
        for location_id, name, distance, inbound in locations:
            c = Control(location_id=location_id, name=name, distance=distance, inbound=inbound)
            c.save()
            count += 1

    print("Added {} Control records".format(count))


def load_timestamps():
    def timestamp2float(ts):
        hrs, mins, secs = ts.split(':')
        return float(int(hrs)) + int(mins)/60 + int(secs)/3600

    f = open("../data/results.json")
    count = 0

    controls = list(Control.objects.all())
    controls.sort(key=lambda x: x.id)
    with transaction.atomic():
        for record in f:
            r = json.loads(record)
            plaque = r["plaque"]
            results = r["results"]
            results = results[:5] + results[15:16] + results[5:8] + results[16:17] + results[8:16]
            for control, result in zip(controls, results):
                if result != "":
                    t = Timestamp(plaque=plaque, control=control, timestamp=timestamp2float(result))
                    t.save()
                    count += 1

    print("Added {} Timestamp records".format(count))


def load_all():
    load_rider_data()
    load_control_locations()
    load_timestamps()
