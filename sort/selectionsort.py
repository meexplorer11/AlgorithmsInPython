def sort(a):
    for i in range(len(a)):
        min_idx = i
        
        for j in range(i+1, len(a)):
            if a[j] < a[i]:
                min_idx = j
        
        a[i], a[min_idx] = a[min_idx], a[i]       



a = [5, 2, 4, 3, 1, 6]

print(f"Before sort->{a}")

sort(a)

print(f"After sort ->{a}")