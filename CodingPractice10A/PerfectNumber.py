n=int(input())
sum_of = 0
for i in range(1,n):
    if n % i ==0:
        sum_of = sum_of + i
if sum_of == n:
    print("Perfect Number")
else:
    print("Not a Perfect Number")