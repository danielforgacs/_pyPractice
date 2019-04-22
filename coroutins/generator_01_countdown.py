def countdown(start):
    while start > 0:
        yield start
        start -= 1


for k in countdown(start=5):
    print(k)
