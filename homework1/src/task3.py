## Create a new file named task3.py. Create an if statement to check if a given number is positive, negative, or zero. 

## Implement a for loop to print the first 10 prime numbers (you may need to research how to calculate prime numbers). 

## Create a while loop to find the sum of all numbers from 1 to 100. Write pytest test cases to verify the correctness 
## of your code for each control structure.

def test_num_value(num):
    if (num > 0):
        return "Positive!"
    elif (num < 0):
        return "Negative!"
    else:
        return "Zero!"

def test_prime_print(number):
    for num in range(1, number):
        if num > 1:  # Prime numbers are greater than 1
            is_prime = True
            # Check for factors from 2 up to the square root of num
            # Optimizing the inner loop by checking up to the square root
            # significantly improves performance for larger numbers.
            for i in range(2, int(num**0.5) + 1): 
                if (num % i) == 0:
                    is_prime = False
                    break  # If a factor is found, it's not prime, so break the inner loop
            if is_prime:
                print(num)
                
def test_while_sum():
    sum = 0
    i = 1
    while i <= 100:
        sum += i
        i += 1
    print(sum)
        
def main():
    number = 1
    test_num_value(number)
    number = -1
    test_num_value(number)
    number = 0
    test_num_value(number)
    
    number = 30
    test_prime_print(number)
    
    test_while_sum()
    
if __name__ == '__main__':
    main()

'''
# test_task3.py
import task3

def test_check_number():
    assert task3.check_number(5) == "positive"
    assert task3.check_number(-3) == "negative"
    assert task3.check_number(0) == "zero"

def test_first_n_primes():
    assert task3.first_n_primes(10) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert task3.first_n_primes(5) == [2, 3, 5, 7, 11]

def test_sum_to_n():
    assert task3.sum_to_n(100) == 5050
    assert task3.sum_to_n(10) == 55
'''