from MathHandler import miller_Rabin_Primality_Test
import random
def encrypt_char():
    return


def encrypt_str():
    return

# will use it for generating two primes p and q
def prime_num_generator(digits: int = 3):
    if digits < 1:
        raise ValueError("Number of digits must be at least 1.")
    
    lower_bound = 10**(digits - 1)
    upper_bound = 10**digits - 1
    
    prime = random.randint(lower_bound, upper_bound)  
    while not miller_Rabin_Primality_Test(prime, 10):
        prime = random.randint(lower_bound, upper_bound) 
    
    return prime
    




def public_key_generator():
    return
