import tracemalloc  # Importing the module to track memory allocations

# Normal function to create a list of cubes
# This function creates and returns a full list, consuming more memory
# n: number of cubes to generate
# Returns: list of cubes from 0 to n-1

def create_cubes(n):
    result = []  # Initialize an empty list
    for x in range(n):
        result.append(x**3)  # Append the cube of x to the list
    return result  # Return the complete list

# Measure memory usage for the normal function
tracemalloc.start()  # Start tracing memory allocations
create_cubes(10**6)  # Call the normal function with 1 million elements
current, peak = tracemalloc.get_traced_memory()  # Get current and peak memory usage
print(f"Peak memory usage by normal function: {peak / 10**6:.2f} MB")  # Print peak memory usage in MB
tracemalloc.stop()  # Stop tracing memory allocations

# Generator function to create cubes
# This function yields one cube at a time, using much less memory
# n: number of cubes to generate
# Yields: cubes from 0 to n-1, one at a time

def create_cubes_new(n):
    for x in range(n):
        yield x**3  # Yield the cube of x (does not store all values in memory)

# Measure memory usage for the generator function
tracemalloc.start()  # Start tracing memory allocations
for _ in create_cubes_new(10**6):  # Iterate through the generator (one value at a time)
    pass  # Do nothing, just consume the generator
current, peak = tracemalloc.get_traced_memory()  # Get current and peak memory usage
print(f"Peak memory usage by generator function: {peak / 10**6:.2f} MB")  # Print peak memory usage in MB
tracemalloc.stop()  # Stop tracing memory allocations

# Explanation:
# The normal function stores all cubes in memory at once, leading to high memory usage.
# The generator function yields one value at a time, so memory usage stays low even for large n.
# This demonstrates the memory efficiency of generators in Python.
