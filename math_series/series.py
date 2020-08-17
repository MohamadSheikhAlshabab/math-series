def lucas_check(n):
    if num==0:
        return 2
    elif num==1:
        return 1
    elif num>1:
        return lucas_check(n-1)+lucas_check(n-2)


def fibonacci(n):
    if  num == 0 :
        return 0
    elif num == 1 :
        return 1
    elif num > 1 :
        return fibonacci ( n - 1 ) + fibonacci ( n - 2)
        

def sum_series(n,n2=0, n3=1):
    return lucas_check(n)+fibonacci(n)
