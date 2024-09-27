from MathHandler import square_and_multiply

def decrypt_char(c,privatekey,modulus):
    return chr(square_and_multiply((c),privatekey,modulus))



def decrypt_str(encrypted_values, d, n):
    decrypted_message = []
    for value in encrypted_values:
        decrypted_ascii = square_and_multiply(value, d, n)  
        decrypted_message.append(chr(decrypted_ascii))  
    return ''.join(decrypted_message)
