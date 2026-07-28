# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# Write a Python program that generates multiplication tables using loops
# and functions.
#
# -----------------------------------------------------------------------------
# PART A — Single Table
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Print the multiplication table for that number from 1 to 12.
#
# Expected output (if user enters 5):
#
#   Multiplication Table for 5:
#   5  x  1  =  5
#   5  x  2  =  10
#   5  x  3  =  15
#   ...
#   5  x  12 =  60
#
# -----------------------------------------------------------------------------
# PART B — Bonus: Tables from 1 to N
# -----------------------------------------------------------------------------
# - Ask the user to enter a number N.
# - Print the full multiplication table for every number from 1 to N.
# - Add a separator line (e.g. "---") between each table.
#
# Expected output (if user enters 3):
#
#   Multiplication Table for 1:
#   1  x  1  =  1
#   ...
#   1  x  12 =  12
#   ---------------------------
#   Multiplication Table for 2:
#   2  x  1  =  2
#   ...
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - N must be a positive integer. If the user enters an invalid value,
#   print an error message and stop.
# - Each part must be in its own function (see scaffold below).
# - Complete Part A before attempting Part B.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
 =============================================================================
def multiplication_table(number: int) -> None:
	"""Print multiplication table for number from 1 to 12."""
	print(f"Multiplication Table for {number}:")
	for i in range(1, 13):
		print(f"{number}  x  {i}  =  {number * i}")


def part_a() -> None:
	"""Part A: Ask user for a single number and print its table."""
	try:
		n = int(input("Enter a number: ").strip())
	except Exception:
		print("Invalid input. Expected an integer.")
		return
	multiplication_table(n)


def part_b() -> None:
	"""Part B: Ask user for N and print tables from 1 to N with separators."""
	try:
		n = int(input("Enter N (positive integer): ").strip())
	except Exception:
		print("Invalid input. Expected an integer.")
		return
	if n <= 0:
		print("Invalid input. N must be a positive integer.")
		return
	for num in range(1, n + 1):
		multiplication_table(num)
		if num != n:
			print('-' * 27)


def main() -> None:
	"""Simple menu to run parts A and B."""
	print("Choose option:\n1) Single table\n2) Tables from 1 to N")
	choice = input("Enter 1 or 2: ").strip()
	if choice == '1':
		part_a()
	elif choice == '2':
		part_b()
	else:
		print("Invalid choice.")


if __name__ == '__main__':
	main()
