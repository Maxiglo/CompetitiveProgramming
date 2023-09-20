with open('a.txt', 'r') as f:
    n = int(f.readline())
    data = [int(line.strip()) for line in f.readlines()]
    m = max(data)
    print(data.index(m) + 1)