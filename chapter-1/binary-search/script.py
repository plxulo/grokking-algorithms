def binary_search(list, item):
  low = 0
  high = len(list) - 1

  while low <= high:
    median = (low + high) // 2
    guess = list[median]

    if guess == item:
      return median
    if guess > item:
      high = median - 1
    else:
      low = median + 1
  return None

test_list = [2, 4, 6, 10, 24]
print(binary_search(test_list, 24))  # Should return the index of 24
print(binary_search(test_list, 8))   # Should return None as 8 is not in the list