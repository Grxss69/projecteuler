x, y = 1, 2
even_num = []

while y <= 4_000_000:
    if x % 2 == 0:
        even_num.append(x)
    elif y % 2 == 0:
        even_num.append(y)
# Creates the Fibonacci Sequence
    x += y
    y += x

print(sum(even_num))

