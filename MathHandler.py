# this class will contains methods that will be used in the computation 



# This function implements the Square and Multiply algorithm for modular exponentiation.
# It calculates (a^e) mod n efficiently using binary exponentiation.
def square_and_multiply(a,e,n):
    result = 1
    for h in bin(e)[2:]:
        result = (result**2) % n
        
        if h == '1':
            result = (result*a) % n

    return result


#  This function implements the extended ecludin  algorithm for finding inverse multiplication of x 
# it calculates (e*e^-1) = 1 mod n . it will be used to compute the private key 
def extended_ecludin_algorithm(e,n):
    if e>n:
        a = e
        b= n
    else:
        a = n
        b = e

    quitont = a // b
    reminder = a % b
    t1 = 0
    t2 = 1
    t = t1 - (t2*quitont)

    while reminder > 0:
        a = b
        b = reminder
        quitont = int(a//b)
        reminder = a % b
        t1 = t2
        t2 = t
        t = t1 - (t2*quitont)
        
    if t2 < 0 :
        return round((t2+n))

    else:
        return round(t2)






