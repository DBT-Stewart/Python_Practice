# 1. Print numbers from 1 to 10
i = 1
while i <= 10:
 print(i, end=' ')
 i += 1

# 2. Sum of natural numbers
n = int(input("Enter a number: "))
i = 1
total = 0

while i <= n:
    total += i
    i += 1

print("Sum is:", total)

# 3. Guess the number game
secret = 7
guess = int(input("Guess the number: "))

while guess != secret:
    guess = int(input("Wrong! Try again: "))

print("Correct! You guessed it.")

# 4. Reverse a number
num = int(input("Enter a number: "))
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print("Reversed number is:", rev)
