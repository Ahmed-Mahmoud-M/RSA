# this class will contains methods that will be used in the computation 



# This function implements the Square and Multiply algorithm for modular exponentiation.
# It calculates (a^e) mod n efficiently using binary exponentiation.
def squareAndmultiply(a,e,n):
    result= 1
    for h in bin(e)[2:]:
        result = (result**2)% n
        
        if h == '1' :
            result = (result*a)% n

    return  result



