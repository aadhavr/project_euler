#
def is_palindrome(number):
    if str(number) == str(number)[::-1]:
        return number
    
largest_palindrome = 0

for i in range(100,999):
    for j in range(i, 999):
        product = i * j
        if is_palindrome(product) and product > largest_palindrome:
            largest_palindrome = product

print(largest_palindrome)