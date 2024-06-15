# find the values of the fibonacci sequence
# get the even values of the fibonacci sequence
# add those values


fib_seq = [1,2]

for i in range(3,10000):
    next_number = fib_seq[-1] + fib_seq[-2]
    if next_number > 4000000:
        break
    fib_seq.append(next_number)
                             
# print(fib_seq)

even_fib_seq = []

for i in fib_seq:
    if i % 2 == 0:
        even_fib_seq.append(i)

even_fib_seq=sum(even_fib_seq)
print(even_fib_seq)



