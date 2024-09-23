# this class will contains methods that will be used in the computation 
import random



# This function implements the Square and Multiply algorithm for modular exponentiation.
# It calculates (a^e) mod n efficiently using binary exponentiation.
def square_and_multiply(a:int,e:int,n:int):
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






# this function implements the miller_Rabin_Primality_Test to check the given number is prime or not 
# the algorithm is like the following : 
#  1. FORi = 1 TO s
#  2. choose randoma ε{2,3, ..., p‘-2}
#  3. z ≡a ^r mod p’
#  4. IF z≠1 AND z≠p’-1 THEN
#  5. FOR j = 1TO u-1
#  6. z ≡ z^2 mod p’
#  7. IF z = 1THEN
#  8. RETURN „p‘ is composite“
#  9. IFz ≠p‘-1THEN
#  10. RETURN „p‘ is composite“
#  11. RETURN„p‘ is likely a prime“


def  miller_Rabin_Primality_Test(canditate:int,rounds =10) :
    if canditate < 2:
        return False
    if canditate in (2, 3):
        return True
    if canditate % 2 == 0:
        return False
     
    m = canditate -1
    k =0
    while m%2 == 0:
        m =m//2
        k+=1
    
    for _ in range(rounds):
        _random = random.randint(2,canditate-2)
        b0 = square_and_multiply(_random,int(m),canditate)
        if b0 == 1 or b0 == canditate - 1:
            continue
        
        for _ in range(k-1):
                b0 = square_and_multiply(b0,2,canditate)
                if b0 == 1 : return False
                if b0 == canditate -1 : break
        else: return False

    return True





   
        

   




    