n=int(input())
greatest = 0
for i in range(n):
    m=int(input())
    if m > greatest:
        greatest=m
print(greatest)