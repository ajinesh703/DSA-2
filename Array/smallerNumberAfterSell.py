def count_smaller(nums):
    def sort(enum):
        mid = len(enum) // 2
        if mid:
            left, right = sort(enum[:mid]), sort(enum[mid:])
            for i in range(len(enum))[::-1]:
                if not right or left and left[-1][1] > right[-1][1]:
                    smaller[left[-1][0]] += len(right)
                    enum[i] = left.pop()
                else:
                    enum[i] = right.pop()
        return enum

    smaller = [0] * len(nums)
    sort(list(enumerate(nums)))
    return smaller
