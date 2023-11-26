

def increase(a, b):
    c = a+b
    uni = list(set(c))
    pot = [i**3 for i in uni]
    return pot


k = [15, 36, 86, 95, 0, 36, 85, 24, 53, 75, 25, 74, 90, 18, 24]
j = [16, 85, 25, 86, 14, 9, 3, 15, 74, 14, 79, 53, 90, 42, 74]
print(increase(k, j))
