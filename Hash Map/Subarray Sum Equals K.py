nums = [1, 1, 1]
k = 2
count = 0
sum = 0
map = {0: 1}

for num in nums:
    sum += num
    if (sum - k) in map:
        count += map[sum - k]
    map[sum] = map.get(sum, 0) + 1

print(count)  # Output: 2
