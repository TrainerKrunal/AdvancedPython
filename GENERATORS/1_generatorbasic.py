"""
1_generatorbasic.py
-------------------
This script explains the concept of generators in Python with examples and comments.

Key Concepts:
1. What is a generator?
2. Why do we need generators?
3. How to create and use generators

What is a generator?
---------------------
- A generator is a special type of iterator in Python that allows you to iterate over a sequence of values, but instead of returning all values at once, it yields them one at a time, only as needed.
- Generators are defined using functions and the 'yield' keyword.
- They are memory efficient because they do not store the entire sequence in memory.

Why do we need generators?
--------------------------
- Generators are useful for working with large datasets or streams of data where it is impractical to load everything into memory at once.
- They allow for lazy evaluation, producing items only when requested.
- They make code more readable and efficient for certain use cases (e.g., reading large files, generating infinite sequences).

Example 1: Simple generator function
------------------------------------
"""

def count_up_to(n):
    """
    Generator that yields numbers from 1 to n.
    Each call to next() or each iteration resumes from where it left off.
    """
    num = 1
    while num <= n:
        yield num  # yield returns a value and pauses the function
        num += 1

if __name__ == "__main__":
    print("Using the generator to count up to 5:")
    gen = count_up_to(5)
    for number in gen:
        print(number)

    print("\nDemonstrating memory efficiency:")
    # Compare with a list comprehension (loads all values in memory)
    numbers_list = [x for x in range(1, 1000001)]  # 1 million numbers in memory
    print(f"Length of list: {len(numbers_list)}")

    # Generator does not load all values at once
    def big_gen():
        for i in range(1, 1000001):
            yield i
    big_gen_obj = big_gen()
    print(f"First value from big_gen: {next(big_gen_obj)}")
    print(f"Second value from big_gen: {next(big_gen_obj)}")
    print("...and so on, without using much memory!")

    print("""
Explanation:
- The count_up_to generator yields numbers one by one, pausing after each yield.
- Generators are ideal for large or infinite sequences, as they only compute values as needed.
- This makes them more memory efficient than lists for many use cases.
""")
