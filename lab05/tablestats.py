def read_rows(lines):
    res = []
    for row in lines[1:]:
        if len(row) == len(lines[0]):
            res.append(dict(zip(lines[0], row)))
    return res
