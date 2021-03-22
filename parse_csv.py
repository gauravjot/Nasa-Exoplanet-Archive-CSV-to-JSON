import re
import json

with open("planets_2021.03.21_19.20.54.csv") as file:
    data = list()
    fields = dict()
    for line in file:
        if re.compile("^#.*").match(line):
            # It is a comment in csv file
            imp_data_pattern = re.compile("^#\s?COLUMN\s([a-zA-Z0-9_]+):\s*([a-zA-Z0-9\[\]\./\* ]+)")
            match_result = imp_data_pattern.match(line)
            if match_result:
                fields[match_result.group(1)] = match_result.group(2)
        else:
            data_pattern = re.compile("(.*?)(?:,|$)")
            ml = list()
            for value in re.finditer(data_pattern, line.strip()):
                ml.append(value.group(1))
            data.append(ml)

    columns = list()
    result = list()
    for index, row in enumerate(data):
        if index == 0:
            columns = row.copy()
        else:
            result.append({col:row[i] for i, col in enumerate(columns)})

    with open("result.json","w") as w:
        json.dump(result, w)

