from ast import Return


def is_numPrimo(num):
    if num == 0 or num == 1:
        return False
    
    for i in range(2, num//2):
        if num % i == 0:
            return False
    return True

print(is_numPrimo(13))