def divisible_by_5_and_7_generator(n):
    for num in range(n + 1):
        if num % 5 == 0 and num % 7 == 0:
            yield num
            
            
given_number = 100
result = ','.join(str(num) for num in divisible_by_5_and_7_generator(given_number))
print(result)
