import csv
from pprint import pprint
with open("Trails.csv", mode= "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)


   # for line in csv_reader:
   #     pprint(line)
    lis = []
    for line in csv_reader:
        pprint(line["CONDITION"])
        if line == ["CONDITION"]:
            lis.append(line)
    print(lis)
