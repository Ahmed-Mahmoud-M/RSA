from Encryptor import *
from MathHandler import *
from Decryptor import *
class RSA:
    def __init__(self) -> None:
        print("1. RSA key generation")
        print("2. RSA key calculation")
        print("3. Encryption message/key ")
        print("4. Decryption message/key ")
        print("5.Exit")

        chioce = int(input("choose from above : "))

        if chioce == 1:
           self.rsakeygeneration()
        elif chioce == 2:
            self.rsaCalculationkey()
        elif chioce == 3:
            self.encryptKey()
        elif chioce == 4:
            self.decryptKey()
        elif chioce == 5:
            exit(0)
        else:
            print("Invalid chioce")


    def rsakeygeneration(self):
        # p_digit,q_digit = 3,3
        print()
        p_digit = int(input("Enter first prime digits you want to generate (default is 3) : "))
        q_digit = int(input("Enter second prime digits you want to generate (default is 3) : "))

        p = prime_num_generator(p_digit)
        q = prime_num_generator(q_digit)


        n = p *q
        phi = (p-1) * (q-1)

        e = generate_public_Exponentiation(phi)
        d = extended_ecludin_algorithm(e,phi)
        print("public key [n, e] : ",{n, e})
        print("private key [d] : ", {d})

        print("1.Encrypt char")
        print("2.Encrypt string")

        ch = int(input("choice from above : "))

        if ch == 1 :
            char = input("Enter the char : ")
            if len(char) > 1 :
                encrypt_str()
                return
            print("Encrypted char is: ", encrypt_char(char,e,n))
            # print("decrypted char is: ", decrypt_char(encrypt_char(char,e,n),d,n))
        elif ch ==2 :
            str= input("Enter the string : ")
            print("Encrypted str is: ", encrypt_str(str,e,n))
            # print("decrypted str is: ", decrypt_str(encrypt_str(str,e,n),d,n))


        else:
            print("Invalid chioce")

    def rsaCalculationkey(self):
        p = int(input("enter the first prime number : "))
        q = int(input("enter the second prime number: "))
        n = p *q
        phi = (p-1) * (q-1)

        e = int(input("Enter public exponot : "))
        d = extended_ecludin_algorithm(e,phi)
        print("public key [n, e] : ",{n, e})
        print("private key [d] : ", {d})

        print("1.Encrypt char")
        print("2.Encrypt string")
        print("3.Decrypt char")
        print("4.Decrypt string")


        ch = int(input("choice from above : "))

        if ch == 1 :
            char = input("Enter the char : ")
            if len(char) > 1 :
                encrypt_str()
                return
            print("Encrypted char is: ", encrypt_char(char,e,n))
            # print("decrypted char is: ", decrypt_char(encrypt_char(char,e,n),d,n))  
        elif ch ==2 :
            str= input("Enter the string : ")
            print("Encrypted str is: ", encrypt_str(str,e,n))
            # print("decrypted str is: ", decrypt_str(encrypt_str(str,e,n),d,n))

        elif ch == 3 :
            char = int(input("Enter the character : "))
            print("decrypted char is: ", decrypt_char(char,d,n)) 

        elif ch == 4 :
            encrypted_input = input("Enter the encrypted values (comma-separated integers): ")
    
        
            encrypted_values = list(map(int, encrypted_input.split(',')))
        
        
            decrypted_message = decrypt_str(encrypted_values, d, n)

            print("decrypted message is: ", decrypted_message)
        else:
            print("Invalid input")

    def encryptKey(self):
       e=  int(input("Enter public exponont : "))
       n=  int(input("Enter modulus : "))
       print("encrypt key is: ", encrypt_str(input("Enter the string : "),e,n))

    def decryptKey(self):
        e=  int(input("Enter private key : "))
        n=  int(input("Enter modulus: "))
        encrypted_input = input("Enter the encrypted values (comma-separated integers): ")
    
        
        encrypted_values = list(map(int, encrypted_input.split(',')))
        
        
        decrypted_message = decrypt_str(encrypted_values, d, n)

        print("decrypted message is: ", decrypted_message)


         
            







            
