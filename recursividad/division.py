def div(n,m):
    if m>n:
        return 0
    else:
        return div((n-m),m)+1

print(div(12,2))