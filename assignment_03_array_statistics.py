# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
 =============================================================================
def calculate_sum(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

def calculate_average(numbers):
    total = calculate_sum(numbers)
    return total / len(numbers) if numbers else 0

def find_maximum(numbers):
    if not numbers:
        return None
    max_val = numbers[0]
    for n in numbers:
        if n > max_val:
            max_val = n
    return max_val

def find_minimum(numbers):
    if not numbers:
        return None
    min_val = numbers[0]
    for n in numbers:
        if n < min_val:
            min_val = n
    return min_val

def main():
    try:
        N = int(input("How many numbers? "))
        if N <= 0:
            print("Error: Please enter a positive integer.")
            return

        numbers = []
        for i in range(N):
            num = float(input(f"Enter number {i + 1}: "))
            numbers.append(num)

        print("\nResults:")
        print(f"Sum:     {calculate_sum(numbers)}")
        print(f"Average: {calculate_average(numbers):.1f}")
        print(f"Maximum: {find_maximum(numbers)}")
        print(f"Minimum: {find_minimum(numbers)}")

    except ValueError:
        print("Error: Please enter valid numbers.")

if __name__ == "__main__":
    main()

