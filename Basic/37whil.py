i = 0
while i < 5:
    print(i)
    i += 1

i = 0
while True:
    print(i)
    i += 1
    if i == 5:
        break

# do while
i = 0
while True:
    print(i)       # code block runs at least once
    i += 1
    if i >= 5:     # condition check at the end
        break