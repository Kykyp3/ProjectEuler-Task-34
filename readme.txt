The problem itsefl "called" - "Factorion"

https://en.wikipedia.org/wiki/Factorion

The best description i found on web was there:

https://www.xarg.org/puzzle/project-euler/problem-34/


If we brute-force the task, the question for a good upper and lower bound arises. The problem description excludes 1! and 2! to be valid, since they are not sums. 3 is a reasonable lower bound, but since the factorial of a one-digit number - except 3 itself - has always more than one digit, we can start with 10

For the upper bound it's a bit trickier to find a reasonable value. If we take a number nn, we can bound it's number of digits dd to

10^{d-1} ≤ n < 10^d

I would advise to read this one.


