_ = input()
f = input().split(' ')

for i, a in enumerate(f):
    f[i] = int(a)
    
def main(nuh):
    itogo = 0
    if len(nuh) == 1:
        itogo = nuh[0]
    elif nuh:
        while len(f) != 1:
            min1 = min(f)
            f.remove(min1)
            min2 = min(f)
            f.remove(min2)
            summ = min1 + min2
            f.append(summ)
            itogo += summ
    return itogo
        
print(main(f))