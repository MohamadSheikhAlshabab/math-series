def lucas_check(num):
    if num==0:
        return 2
    elif num==1:
        return 1
    elif num>1:
        return lucas_check(num-1)+lucas_check(num-2)
    print(num)


def fibonacci(num):
    if  num == 0 :
        return 0
    elif num == 1 :
        return 1
    elif num > 1 :
        return fibonacci ( num - 1 ) + fibonacci ( num - 2)
    print(num)
        

def sum_series(num,num2=0, num3=1):
    return lucas_check(num)+fibonacci(num)
