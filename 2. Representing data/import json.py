import json


with open ("cso.json", "rt") as fp:
    csodataset = json.load(fp)
    print (csodataset[0])