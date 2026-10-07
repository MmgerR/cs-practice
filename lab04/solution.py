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

def ranking(names, scores):
    indices = list(range(len(names)))    
    indices.sort(key=lambda i: scores[i], reverse=True)
    return [names[i] for i in indices]

def above_average(names, scores):
    result = []
    for j in range(len(scores)):
        if scores[j] > average(scores):
            result.append(names[j])
    return result

if __name__ == '__main__':
    names =  ["Аня", "Боря", "Вика"]
    scores = [7.0,   9.0,    9.0]
    print(winner(names, scores))
    print(average(scores))
    print(ranking(names, scores))
    print(above_average(names, scores))