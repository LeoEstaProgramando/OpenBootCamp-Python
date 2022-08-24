def is_añoBisiesto(año):
    if (año % 4 == 0 and año % 100 != 0) or año % 400 == 0:
        return True
    else:
        return False

print(is_añoBisiesto(1600))