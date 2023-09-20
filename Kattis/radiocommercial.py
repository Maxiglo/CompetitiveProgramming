def max_subarray(v, p):
    def max_crossing_subarray(v, low, mid, high, p):
        left_sum = float('-inf')
        sum = 0
        for i in range(mid, low - 1, -1):
            sum += v[i] - p
            left_sum = max(left_sum, sum)

        right_sum = float('-inf')
        sum = 0
        for i in range(mid + 1, high + 1):
            sum += v[i] - p
            right_sum = max(right_sum, sum)

        return left_sum + right_sum

    def max_subarray_helper(v, low, high, p):
        if low == high:
            return max(0, v[low] - p)
        
        mid = (low + high) // 2

        left_max = max_subarray_helper(v, low, mid, p)
        right_max = max_subarray_helper(v, mid + 1, high, p)
        crossing_max = max_crossing_subarray(v, low, mid, high, p)

        return max(left_max, right_max, crossing_max)

    return max_subarray_helper(v, 0, len(v) - 1, p)

n, p = map(int, input().split())
v = list(map(int, input().split()))
result = max_subarray(v, p)
print(result)
