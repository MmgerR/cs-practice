bar = float(input('Введите пороговое значение: '))
n = int(input('Введите количество записей: '))
print('Введите значения:')
err_count = 0
bar_count = 0
max_val = 0
mid_val = 0
for i in range(n):
    val = input()
    if val == 'error':
        err_count += 1
        continue
    else:
        if float(val) > bar:
            bar_count += 1
        if float(val) > max_val:
            max_val = float(val)
        if mid_val += float(val)
