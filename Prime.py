# Write a program for extracting the prime number from the list of numbers.

numb = [2,13, 14, 53, 6, 17, 18, 19,9]
prime_numbers = []

for num in numb:
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            prime_numbers.append(num)

print("Prime Numbers : ",prime_numbers)
