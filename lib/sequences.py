#!/usr/bin/env python3

def print_fibonacci(length):
    fib_sequence = []
    if length >= 1:
        fib_sequence.append(0)
    if length >= 2:
        fib_sequence.append(1)
    for i in range(2, length):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    print(fib_sequence)
    
print_fibonacci(9)