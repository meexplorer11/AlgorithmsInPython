size = int(input("Enter size: "))
print(size)

nums = [r for r in range(size)]
print(nums)

def isConnected(p, q):
    if nums[p] == nums[q]:
        print("Connected")
        return True
    else:
        print("Not connected")    
        return False

def union(p, q):
    if isConnected(p, q):
        print("Already connected")
        return
    else:
        print("Marking union")

    pVal = nums[p]
    qVal = nums[q]

    for index, value in enumerate(nums):
        if value == pVal:
            nums[index] = qVal


isConnected(2, 5)
union(2, 5)      
print(nums)
isConnected(2, 5)  