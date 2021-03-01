
largest: None = None
print("Before:", largest)
for interval in [3, 41, 12, 9, 74, 15]:
    if largest is not None and largest >= interval:
        pass
    else:
        largest = interval
    print('Loop:', interval, largest)
print('Largest:', largest)
