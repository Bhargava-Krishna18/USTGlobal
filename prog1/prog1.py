
# generator to print the numbers which can be divisible by 5 and 7 between 0 and given number n
def div_5_7(n):
    for num in range(n + 1):
        if num % 5 == 0 and num % 7 == 0:
            yield num
            
            
given_number = 100
result = ','.join(str(num) for num in div_5_7(given_number))
print(result)



# function that interleaves 2 strings

def inters(str_1, str_2):
    inter = ''.join(s1 + s2 for s1, s2 in zip(str_1, str_2))
    if len(str_1) > len(str_2):
        inter += str_1[len(str_2):]
    elif len(str_1) < len(str_2):
        inter += str_2[len(str_1):]
    return inter


str_1 = "AAAA"
str_2 = "1234567"
inter = inters(str_1, str_2)
print(inter)  
