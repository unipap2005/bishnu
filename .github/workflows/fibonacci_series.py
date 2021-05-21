def fibonacci(n):
    fibo_series=[0,1]
    i,j=0,1
    while(n-2):
        k=i+j
        fibo_series.append(k)
        i=j
        j=k
        n-=1
    return(fibo_series)

print(fibonacci(10))
