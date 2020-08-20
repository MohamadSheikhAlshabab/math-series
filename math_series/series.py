import sys
sys.setrecursionlimit(10**9) 

def lucas_check(n):
    if n==0:
        return 2
    elif n==1:
        return 1
    elif n>1:
        return lucas_check(n-1)+lucas_check(n-2)


def fibonacci(n):
    if  n == 0 :
        return 0
    elif n == 1 :
        return 1
    elif n > 1 :
        return fibonacci ( n - 1 ) + fibonacci ( n - 2)


def sum_series(n,n2=0, n3=1):
    if n2==0 and n3==0:
        return fibonacci(n)
    elif n2==2 and n3==1 :
        return lucas_check(n)
    else:
        if n2<n3:
            if n == n2:
                return n2
            elif n == n3 :
                return n3
            else:
                return sum_series ( n-1 , n2  , n3  ) + sum_series ( n-2 , n2  , n3 )
            

# def print_out():
#     num=int(input())
#     num2=int(input())
#     num3=int(input())
#     lucas="Lucas of {} = ",lucas_check(num)
#     fibo="fibonacci of {} = ",fibonacci(num)
#     sum_s="sum_series of {} {} {} = ",sum_series(num,num2,num3)
#     print(str(lucas).format(num))
#     print(str(fibo).format(num))
#     print(str(sum_s).format(num,num2,num3))
# print(sys.getrecursionlimit())
# print_out()