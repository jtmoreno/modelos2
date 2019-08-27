

def fibo(b):
    if b<=2:
        return 1
    if b>2:
        return fibo(b-1)+fibo(b-2) 

a=int(input())
repe=fibo(a)

print("el numero que ingreso es: "+repr(a)+" el numero en la serie de fibonachi es:"+ repr(repe))