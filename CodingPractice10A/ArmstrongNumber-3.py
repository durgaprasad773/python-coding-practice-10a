n=input()
length = len(n)
sum_of=0
for i in n:
    sum_of = sum_of + (int(i) ** length)
if sum_of == int(n):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")