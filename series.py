def fibonacci(n): 
    """ accepts fibonacci number, returns nth number """
    """ Using the fibonacci number sequence"""
    if n==1: 
      return 0
    elif n==2: 
      return 1
    else: 
      return fibonacci(n-1)+fibonacci(n-2)  
  
def lucas(n):
    """ accepts lucas number, returns nth number """
    """ Using the lucas number sequence"""
    if n==1: 
      return 2
    elif n==2: 
      return 1
    else: 
      return lucas(n-1)+lucas(n-2)  

def sum_series(n, first=0, second=1):
    if n==1: 
      return first
    elif n==2: 
      return second
    elif n==0:
      return 0
    else: 
      return sum_series(n-second)+sum_series(n-first) 

