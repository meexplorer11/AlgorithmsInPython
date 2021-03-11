def sort(a):
    size = len(a)
    for i in range(size):
        key = a[i]
        j = i-1;
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j = j-1
        a[j+1] = key    


a = [5, 2, 4, 3, 1, 6]

print(f"Before sort->{a}")

sort(a)

print(f"After sort ->{a}")