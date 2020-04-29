# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.


def factorial(x):
    factorial = 1
    for i in range(1,x+1):
        factorial *= i
    return factorial

f = [factorial(0),
factorial(1),
factorial(2),
factorial(3),
factorial(4),
factorial(5),
factorial(6),
factorial(7),
factorial(8),
factorial(9)]

def count_digit_factorials(x):
	sum = 0
	while x>0:
		sum += f[x%10]
		x //= 10
	return sum

def solution():
	sum = 0
	for i in range(10,1499999):
		print("Число:{}".format(i))
		print("Сумма факт:{}".format(count_digit_factorials(i)))
		if i == count_digit_factorials(i):
			sum += i
	return sum

print(solution())