names =  ["Аня", "Боря", "Вика"]
scores = [7.0,   9.0,    9.0]

def winner(names, scores):
    number = 0
    for i in scores:
        if i > number:
            number = i
    return names[scores.index(number)]

def average(scores):
    if len(scores) == 0:
        return 0
    return round(sum(scores)/len(scores), 2)