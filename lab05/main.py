from tablestats import *

if __name__ == '__main__':
    file = input().strip()
    with open(file, encoding='utf-8') as f:
        lines = [line.strip().split(',') for line in f if line.strip() != '']

    table = read_rows(lines)
    counts = count_types(table)
    print(table)
    print(count_types(table))
    print(total_minutes(table, 'ошибка'))
    print(to_csv(counts))

    with open("summary.csv", "w", encoding="utf-8") as out:
        out.write(f'{len(table)}\n{len(counts)}\n{total_minutes(table, "ошибка")}')