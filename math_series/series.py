import sys
sys.setrecursionlimit(10**9) 

def lucas_check(n):
    """
    The Lucas numbers or Lucas series are an integer sequence named after the mathematician François Édouard Anatole Lucas (1842–91).
    The Lucas sequence has the same recursive relationship as the Fibonacci sequence,
    where each term is the sum of the two previous terms, but with different starting values.
    This produces a sequence where the ratios of successive terms approach the golden ratio, 
    and in fact the terms themselves are roundings of integer powers of the golden ratio.
    """
    if n==0:
        return 2
    elif n==1:
        return 1
    elif n>1:
        return lucas_check(n-1)+lucas_check(n-2)


def fibonacci(n):
    """
    the Fibonacci numbers, commonly denoted Fn, form a sequence, called the Fibonacci sequence,
    such that each number is the sum of the two preceding ones, starting from 0 and 1.
    """
    if  n == 0 :
        return 0
    elif n == 1 :
        return 1
    elif n > 1 :
        return fibonacci ( n - 1 ) + fibonacci ( n - 2)


def sum_series(n,n2=0, n3=1):
    """
    This is generic series function, if the default arguments are 0,1 respectively then 
    will return Fibonacci series, else if the arguments are 2,1 respectively then
    will return Lucas series, else that it's a generic series.

    """
    if n<0 and n2<0 and n3<0:
        print (" You Should insert a positive numbers")
    elif n2==0 and n3==1:
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
        else: 
            print (" You Should insert the second number less than the third number, (n2 < n3)")
    # return sum_series ( n-1 , n2  , n3  ) + sum_series ( n-2 , n2  , n3 )
            

def print_out():
    num=int(input("Insert the number 'n' of the series : "))
    num2=int(input("Insert the number 'n2' of the sum series : "))
    num3=int(input("Insert the number 'n3' of the sum series : "))
    lucas="Lucas of {} = ",lucas_check(num)
    fibo="fibonacci of {} = ",fibonacci(num)
    sum_s="sum_series of {}, {}, {}= ",sum_series(num,num2,num3)
    print(str(lucas).format(num))
    print(str(fibo).format(num))
    print(str(sum_s).format(num,num2,num3))
print_out()