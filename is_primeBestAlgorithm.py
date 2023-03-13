import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True
if __name__ == "__main__":
    try:
        n = int(input("Input : "))
        print("Answer",is_prime(n))
    except:
        print("Failed")
