l = ["k","i","m","c","h","i"]
L = ["k","i","m","c","h","i"]
n = 0

while True:
    i = input()
    for c in l:
        if c == i:
            n += 1
            print(6 - n,"left")
            l.remove(i)
            
    
    if n == 6:break
    else:continue
        
print(*L)
