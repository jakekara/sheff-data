#!/usr/bin/env python2

""" Convert spreadsheet to proper json structure for fancy table """

import json

CSV_SOURCE = "../data/hopefully-clean-odds.csv"
LAST_YEARS = "last_years.json"

obj = json.loads(open(LAST_YEARS).read())

old_data = obj["data"]
obj["data"] = {}

cols = map(lambda x: str(x["title"]), obj["column_names"])

def examine_data():

    """ print out what the data looks like so we can match it """

    print json.dumps(obj,indent=2)

    print json.dumps(old_data)[:100] + "..."

    print cols
    

examine_data()
