n=input()
k=len(n)
sum_of = 0
for i in n:
    sum_of = sum_of + (int(i) ** k)
print(sum_of)