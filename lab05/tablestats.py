def read_rows(lines):
    res = []
    for row in lines[1:]:
        if len(row) == len(lines[0]):
            res.append(dict(zip(lines[0], row)))
    return res

def count_types(rows):
    res = {}
    for row in rows:
        for key in row:
            if key == 'тип':
                if row[key] in res.keys():
                    res[row[key]] += 1
                else:
                    res[row[key]] = 1
    return res