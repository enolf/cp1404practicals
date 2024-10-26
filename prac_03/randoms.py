"""
What did you see on line 1?
19
What was the smallest number you could have seen, what was the largest?
range from 5 to 20, including endpoints

What did you see on line 2?
3
What was the smallest number you could have seen, what was the largest?
range from 3 to 9
Could line 2 have produced a 4?
No 4 is an even number and this line only printed numbers going from 3 in 2s i.e. odd numbers between 3 and 10

What did you see on line 3?
4.919240440522291
What was the smallest number you could have seen, what was the largest?
range from 2.5 to 5.5
Write code, not a comment, to produce a random number between 1 and 100 inclusive."""
import random

print(random.randint(1, 100))
