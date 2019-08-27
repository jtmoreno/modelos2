a=2
b=8

def potencial(a,b):
    if a==0:
        return 1
    elif a==1:
        return b
    else :
        return potencial(a-1,b)*b

print("el resultado es:" + repr(potencial(a,b)))