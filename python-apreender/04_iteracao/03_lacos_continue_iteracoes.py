while True:
    line = input("add:")
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print("Done")
