def fact(n):
    if n==1:
        return 1
    else:
        return(n*fact(n-1))
n=int(input("enter the number:"))
print("the factorial of a number is:",fact(n))
 
def fib(n):
     if n<=1:
         return n
     else:
        return (fib(n-1)+fib(n-2))
n=int(input("enter the range:"))
print("the fibonacci value is:",fib(n))