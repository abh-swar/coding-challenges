w = input()
try:
    w = int(w)
    if w<1 or w>100:
        print("NO")
    elif w%2 == 1 or w == 2:
        print("NO")
    else:
        print("YES")
except:
    print("NO")