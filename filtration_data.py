data = [
    [100, 110, 120],
    [400, 500, 600],
    [130, 140, 150]
    ]

list = []

for row in data:
    for item in row:
        if item > 190:
            list.append(item)