import json

f = open('D:\\Users\\Misha\\Python\\Stat\\Tsk1\\input.txt', 'r', encoding='utf-8')
arr = f.readline().split(', ')
print(arr)
col = 0
a = []
b = []

for i in range(10):
    start = 15 + i * 0.75
    end = 15 + (i + 1) * 0.75
    coli = 0
    for k in arr:
        if float(k) > start and float(k) <= end:
            coli += 1
    col += coli
    a.append(coli)

print(a)

for i in range(10):
    b.append(round(a[i] / col, 3))

with open('D:\\Users\\Misha\\Python\\Stat\\Tsk1\output.txt', 'w') as fw:
    json.dump(b, fw)

