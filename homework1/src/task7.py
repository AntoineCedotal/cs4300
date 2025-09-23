## Use pip package manager to add a Python package of your choice to your project (numpy).
## Create a new file named task7.py and write a Python script that demonstrates
## how to use the chosen package to perform a specific task or function. Implement pytest test cases
## to verify the correctness of your code when using the package.

import numpy as np

def compute_statistics(numbers):
    """
    Compute mean, median, and standard deviation of a list or array of numbers.
    Returns a dictionary with keys: 'mean', 'median', 'std'.
    """
    arr = np.array(numbers)
    return {
        "mean": np.mean(arr),
        "median": np.median(arr),
        "std": np.std(arr)
    }


if __name__ == "__main__":
    data = [2, 4, 4, 4, 5, 5, 7, 9]
    stats = compute_statistics(data)
    print(f"Data: {data}")
    print(f"Mean: {stats['mean']}")
    print(f"Median: {stats['median']}")
    print(f"Standard Deviation: {stats['std']}")
