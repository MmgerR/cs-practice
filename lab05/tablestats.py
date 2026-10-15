def read_rows(lines: list[str]):
    res = []
    arr = [x.split(',') for x in lines]
    for row in arr[1:]:
        if len(row) == len(arr[0]):
            res.append(dict(zip(arr[0], row)))
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

def total_minutes(rows, kind):
    res = 0
    for row in rows:
        for key in row:
            if row[key] == kind:
                res += float(row['минуты'])
    return round(res, 2)

def to_csv(counts):
    res = 'тип,количество\n'
    for key in sorted(counts.keys()):
        res += f'{key},{counts[key]}\n'
    return res