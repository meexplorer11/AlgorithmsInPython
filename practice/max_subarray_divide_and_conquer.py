def max_crossing_subarray(a, low, mid, high):
    sum = 0
    left_sum = 0
    left_idx = 0

    for i in range(mid, low-1, -1):
        sum = sum+a[i]
        if sum > left_sum:
            left_sum = sum
            left_idx = i

    sum = 0
    right_sum = 0
    right_idx = 0

    for i in range(mid+1, high+1, 1):
        sum = sum + a[i]
        if sum > right_sum:
            right_sum = sum
            right_idx = i

    return (left_idx, right_idx, (left_sum + right_sum))        


def max_subarray(a, low, high):
    
    if low == high:
        return (low, high, a[low])
    else:
        mid = low + (high-low)//2
        
        left_low, left_high, left_sum = max_subarray(a, low, mid)

        right_low, right_high, right_sum = max_subarray(a, mid+1, high)

        cross_low, cross_high, cross_sum = max_crossing_subarray(a, low, mid, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)        



a = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]

left, right, sum = max_subarray(a, 0, len(a)-1)

print(f"Maximum subarray: [{left}, {right}] with sum= {sum}")
