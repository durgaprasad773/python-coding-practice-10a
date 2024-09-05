n=int(input())
sum_of_factors = 0

for i in range(1,n+1):
    if n % i ==0:
        sum_of_factors = sum_of_factors + i 
print(sum_of_factors)