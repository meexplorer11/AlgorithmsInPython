a = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]

left = 0
right = 0
temp = 0
sum = 0
max_sum = 0

for index, item in enumerate(a):
    sum = sum + item

    if sum > max_sum:
        max_sum = sum
        left = temp
        right = index

    if sum < 0:
        sum = 0
        temp = index+1    

print(f"Maximum subarray: [{left}, {right}] with sum= {max_sum}")