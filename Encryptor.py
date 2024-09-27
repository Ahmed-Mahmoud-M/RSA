from MathHandler import miller_Rabin_Primality_Test,square_and_multiply
import random
from math import gcd



def encrypt_char(c,publicExponent,modulus):
    return square_and_multiply(ord(c),publicExponent,modulus)


def encrypt_str(plain_text,e,n):
        encrypted_values = []
        for char in plain_text:
            ascii_value = ord(char) 
            encrypted_value = square_and_multiply(ascii_value, e, n)  
            encrypted_values.append(encrypted_value)
        return encrypted_values

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



def generate_public_Exponentiation(phi):
    
    result =0 

    while gcd(result, phi) != 1:
        result = random.randint(1,phi)


    return result    
    




