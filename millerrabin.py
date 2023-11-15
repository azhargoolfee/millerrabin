#Name : Azhar Goolfee
import random
 
def primality_test(n, a): #performs primality test using the two properties of prime number
    q, k = n - 1, 0         #calculates the value of k and q (k>0 & q odd)
    while not q % 2:        #n - 1 = 2^k * q
        q, k = q >> 1, k + 1
   
    if pow(a, q, n) == 1:     #checks if a^q mod 1 is congruent to 1
        return True
        
    for j in range(k):      #loops k times
        if pow(a, 2**j * q, n) == n - 1:    #checks if a ^ (2^j * q) mod n is congruent to n - 1
            return True

    return False #if both properties fail (n is composite)
    
def miller_rabin(n, t):
    random_num = random.SystemRandom() 
    for i in range(t):      #confidence t = 6
        a = random_num.randrange(1, n - 1)  #generates a random number 1 < a < n-1
        if not primality_test(n, a):    #if the number doesnt pass the primality test
            return False       
    return True     #n is probably prime (passes primality prime)
    

def find_prime(bits, t):    #generates random 15-bit odd number and calls Miller Rabin function
    bits = bits - 1
    while True:
        random_bit = random.randint(0, 2**bits - 1)     #generates random number
        a = random_bit | (1 << bits)    #LSB is set to 1 (becomes odd)
        if miller_rabin(a,t):   #calls Miller Rabin function with a and t = 6
            return a
            
if __name__ == "__main__":  #main function
    for i in range(10):
        p = find_prime(15, 6) #calls function with args no. of bits 15 and confidence 6
        print(p)    #prints prime number