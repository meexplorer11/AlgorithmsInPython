size = int(input("Enter size: "))

items = [n for n in range(size)]
print(items)

def root(p):
    while p != items[p]:
        p = items[p]

    print(f"Root={p}")
    return p


def isConnected(p, q):
    return root(p) == root(q)


def logConnected(flag):
    if flag:
        print("Connected")             
    else:
        print("Not Connected")    


def union(p, q):
    proot = root(p)
    qroot = root(q)

    items[qroot] = proot


logConnected(isConnected(2, 5))
union(2, 5)      
print(items)
logConnected(isConnected(2, 5))
