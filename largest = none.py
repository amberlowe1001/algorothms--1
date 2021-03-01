import

largest: int = int
print("Before:", largest)
for interval in [3, 41, 12, 9, 74, 15]:
    if largest is None or largest < interval:
        largest = interval
    print('Loop:', interval, largest)
print('Largest:', largest)
