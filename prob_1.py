sum_mult_3_5 = []

for i in range(1,1000):
    if i % 3 == 0 or i % 5 == 0:
        sum_mult_3_5.append(i)
    
sum_mult_3_5 = sum(sum_mult_3_5)


print(sum_mult_3_5)