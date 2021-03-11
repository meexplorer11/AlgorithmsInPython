def merge(a, start, mid, end):
    n1 = mid - start +1
    n2 = end - mid

    l = [0] * (n1)
    r = [0] * (n2)

    for i in range(0, n1):
        l[i] = a[start+i]

    for i in range(0, n2):
        r[i] = a[mid+1+i]  

    l_idx = 0
    r_idx = 0
    k = start

    while l_idx < n1 and r_idx < n2:
        if l[l_idx] <= r[r_idx]:
            a[k] = l[l_idx]
            l_idx = l_idx+1
        else:
            a[k] = r[r_idx]
            r_idx = r_idx+1

        k = k+1   

    while l_idx < n1:
        a[k] = l[l_idx]
        l_idx = l_idx+1
        k = k+1

    while r_idx < n2:
        a[k] = r[r_idx]
        r_idx = r_idx+1
        k = k+1    



def sort(a, start, end):
    if start < end:
        mid = (start + (end-1))//2
        sort(a, start, mid)
        sort(a, mid+1, end)
        merge(a, start, mid, end)
        

a = [5, 2, 4, 3, 1, 6]

print(f"Before sort->{a}")

sort(a, 0, len(a)-1)

print(f"After sort ->{a}")