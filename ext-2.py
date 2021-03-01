from typing import List

import app as app

numbers = [11, 21, 19, 18, 46]

# start parameter is not provided
sumList = sum(numbers)
print(sumList)

# start = 10
sumList = sum(numbers, 10)
print(sumList)
